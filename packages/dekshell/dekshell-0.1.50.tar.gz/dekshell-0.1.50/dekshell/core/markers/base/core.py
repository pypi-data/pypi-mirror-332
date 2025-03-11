import os
import sys
from types import NoneType
from dektools.output import obj2str
from dektools.str import hex_random
from . import MarkerBase, TransformerMarker, ExitException


class MarkerEnv:
    def __init__(self, shell_exec, shell_cmd, context):
        self.shell_exec = shell_exec
        self.shell_cmd = shell_cmd
        self.context = context
        self.inner = {}
        self.__environ = {}

    def __str__(self):
        return obj2str(
            dict(shell_exec=self.shell_exec, shell_cmd=self.shell_cmd, context=self.context))

    @property
    def eval_locals(self):
        return self.context

    def add_inner_item(self, k, v):
        self.inner[k] = v

    def remove_inner_item(self, name):
        if isinstance(name, str):
            self.inner.pop(name, None)
        else:
            for x in name:
                self.remove_inner_item(x)

    def get_inner_item(self, name, default=None):
        return self.inner.get(name, default)

    def remove_variable(self, name):
        if isinstance(name, str):
            self.context.pop(name, None)
        else:
            for x in name:
                self.remove_variable(x)

    def add_variable(self, k, v):
        self.context[k] = v

    def add_variable_temp(self, value):
        while True:
            name = f'_temp_var_{hex_random(16)}'
            if name not in self.context:
                break
        self.add_variable(name, value)
        return name

    def environ(self):
        environ = os.environ.copy()
        environ.update(self.__environ)
        return environ

    @property
    def environ_pointer(self):
        return self.__environ


class PlaceholderMarker(MarkerBase):
    tag_head = ""


class MarkerNode:
    def __init__(self, marker, command, index, parent=None, command_old=None, payload=None):
        self.marker = marker
        self.command = command
        self.command_old = command_old
        self.index = index
        self.parent = parent
        self.children = []
        self.payload = payload

    def __repr__(self):
        return f'Node({self.marker.__class__.__name__})'

    def clone(self):
        node = self.__class__(
            self.marker, self.command, self.index, self.parent, self.command_old, self.payload)
        node.children = self.clone_children(node)
        return node

    def clone_children(self, parent=None):
        result = []
        for child in self.children:
            node = child.clone()
            node.parent = parent or self
            result.append(node)
        return result

    @property
    def debug_info(self):
        def walk(node):
            return dict(
                marker=node.marker,
                command=node.command,
                index=node.index,
                children=[walk(child) for child in node.children]
            )

        return obj2str(walk(self))

    def is_type(self, *markers_cls):
        return isinstance(self.marker, tuple(markers_cls))

    def add_child(self, node):
        node.parent = self
        self.children.append(node)
        return node

    def bubble_continue(self, env, node):
        cursor = self
        while cursor:
            # result is (x, [y]) =>  x: location exec depth, [y]: insert to loop
            result = cursor.marker.bubble_continue(env, cursor, node)
            if result is None:
                cursor = cursor.parent
            else:
                return result
        return None

    @classmethod
    def exec_nodes(cls, env, marker_set, nodes):
        while nodes:
            node = nodes.pop(0)
            result = node.bubble_continue(env, node)
            if result is not None:
                return result
            else:
                try:
                    nodes_changed = node.marker.exec(
                        env,
                        node.marker.translate(env, node.command or ''),
                        node, marker_set
                    )
                except ExitException:
                    raise
                except Exception as e:
                    sys.stderr.write(f"Execute error {node.marker}:\n\
                    command=> {node.command if node.command_old is None else node.command_old}\n\
                    line=> {node.line_number}\n\
                    env=>\n\
                    {env}")
                    raise e from None
                result = cls.exec_nodes(
                    env,
                    marker_set,
                    node.children[:] if nodes_changed is None else nodes_changed
                )
                if result is not None:
                    node_cursor, node_loop_list = result
                    if node is node_cursor:  # location of the depth
                        nodes[:0] = node_loop_list
                    else:
                        return result

    def exec(self, env, marker_set):
        self.exec_nodes(env, marker_set, [self])

    def walk(self, cb, depth=0):
        cb(self, depth)
        for child in self.children:
            child.walk(cb, depth + 1)

    @classmethod
    def root(cls):
        return cls(PlaceholderMarker(), None, None)

    @property
    def line_number(self):
        if self.index is None:
            return None
        return self.index + 1


class MarkerSet:
    node_cls = MarkerNode
    env_cls = MarkerEnv
    transformer_cls = TransformerMarker

    def __init__(self, markers_cls):
        markers = []
        self.markers_branch_set = set()
        for marker_cls in markers_cls:
            markers.append(marker_cls())
            for branch_cls in marker_cls.final_branch_set:
                self.markers_branch_set.add(branch_cls)
        self.markers = self.transformer_cls.inject(markers)

    def is_marker_branch(self, marker):
        return marker.__class__ in self.markers_branch_set

    def find_marker_by_cls(self, marker_cls):
        for marker in self.markers:
            if isinstance(marker, marker_cls):
                return marker

    def find_marker_by_command(self, command):
        for marker in self.markers:
            if marker.recognize(command):
                return marker

    def generate_tree(self, commands):
        stack = [self.node_cls.root()]
        for index, command in enumerate(commands):
            marker = self.find_marker_by_command(command)
            while isinstance(marker, stack[-1].marker.tag_tail or NoneType):
                node_tail = stack.pop()
                if not self.is_marker_branch(node_tail.marker):
                    break
            parent = stack[-1]
            marker = marker.transform(parent.marker)
            node = self.node_cls(marker, command, index)
            parent.add_child(node)
            if marker.tag_tail is not None:  # block command
                stack.append(node)
        if len(stack) != 1:
            raise Exception(f'Stack should have just a root node in final: {stack}')
        return stack[0]

    def exec(self, commands, shell_exec, shell_cmd, context):
        try:
            root = self.generate_tree(commands)
            root.exec(self.env_cls(shell_exec, shell_cmd, context or {}), self)
        except ExitException:
            pass

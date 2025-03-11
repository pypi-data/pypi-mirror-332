from .base import MarkerBase, MarkerWithEnd
from .empty import EmptyMarker


class ExecMarker(MarkerBase):
    tag_head = '<'

    def exec(self, env, command, marker_node, marker_set):
        args = self.split_raw(command, 1, self.tag_head)
        if args[1]:
            self.eval(env, args[1])


class ExecLinesMarker(MarkerWithEnd):
    tag_head = '<<'

    def exec(self, env, command, marker_node, marker_set):
        code = self.get_inner_content(env, marker_node)
        self.eval_codes(env, code)
        return []


class ExecCmdCallMarker(MarkerBase):
    tag_head = '>'

    def exec(self, env, command, marker_node, marker_set):
        args = self.split_raw(command, 1, self.tag_head)
        if args[1]:
            args = self.split_raw(args[1], 1)
            func = args[0]
            args, kwargs = self.cmd2ak(self.split(args[1]))
            self.call_func(env, func, *args, **kwargs)


class ExecCmdCallLinesMarker(MarkerWithEnd):
    tag_head = '>>'
    cmd_call_marker_cls = ExecCmdCallMarker
    targets_marker_cls = (EmptyMarker, )

    def exec(self, env, command, marker_node, marker_set):
        marker = marker_set.find_marker_by_cls(self.cmd_call_marker_cls)
        result = []
        for child in marker_node.children:
            if child.is_type(*self.targets_marker_cls):
                node = marker_set.node_cls(
                    marker,
                    self.cmd_call_marker_cls.tag_head + ' ' + child.command,
                    child.index,
                    marker_node,
                    child.command
                )
                result.append(node)
            else:
                result.append(child)
        return result

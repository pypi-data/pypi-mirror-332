import os
import re
import shlex
import functools
from dektools.str import deep_format, split_table_line
from dektools.common import classproperty
from dektools.shell import shell_output, shell_exitcode
from ....utils.serializer import serializer
from ....utils.cmd import cmd2ak

cmd_call_prefix = '>'


class MarkerBase:
    tag_head = None
    tag_head_args = None
    tag_head_re = None
    tag_head_re_args = None
    tag_tail = None
    branch_set = set()

    var_name_anonymous = '_'

    trans_marker_command_output = '>>'
    trans_marker_command_rc = '>'
    trans_marker_decode = '//'
    trans_marker_encode = '/'
    trans_marker_env_full = '$$'
    trans_marker_env = '$'
    trans_marker__set = '|'.join((re.escape(x) for x in [
        trans_marker_command_output,
        trans_marker_command_rc,
        trans_marker_decode,
        trans_marker_encode,
        trans_marker_env_full,
        trans_marker_env,
    ]))
    trans_marker__as_var = '='
    trans_marker__ignore = '?'
    trans_marker__begin = "{"
    trans_marker__end = "}"
    trans_marker__escape = "\\"

    VALUE_UNSET = type('Unset', (), {})

    @classmethod
    def get_tag_match(cls):
        if cls.tag_head is not None:
            s = cls.tag_head if cls.tag_head_args is None else cls.tag_head % cls.tag_head_args
        else:
            s = None
        if cls.tag_head_re is not None:
            r = cls.tag_head_re if cls.tag_head_re_args is None else cls.tag_head_re % cls.tag_head_re_args
        else:
            r = None
        return s, r

    def recognize(self, command):
        command = self.strip(command)
        s, r = self.get_tag_match()
        if s is not None:
            if command.startswith(s):
                rule = re.compile('[0-9a-zA-Z_]')
                return not (s and rule.match(s[-1]) and rule.match(command[len(s):len(s) + 1]))
            return False
        elif r is not None:
            return bool(re.match(r, command))
        return False

    def transform(self, parent):
        return self

    def bubble_continue(self, env, marker_set, marker_node_self, marker_node_target):
        return None

    def exec(self, env, command, marker_node, marker_set):
        pass

    def exit(self):
        raise ExitException()

    def set_var(self, env, array, index, value):
        self.set_var_raw(env, self.get_item(array, index, self.var_name_anonymous), value)

    @staticmethod
    def set_var_raw(env, name, value):
        env.add_variable(name, value)

    @staticmethod
    def remove_var(env, name):
        env.remove_variable(name)

    def call_func(self, env, func_name, *args, **kwargs):
        args, kwargs = self.var_map_batch(env, *args, **kwargs)
        func = env.context.get(func_name)
        if func is None:
            func = self.eval(env, func_name)
        return func(*args, **kwargs)

    def cmd_call(self, env, s):
        argv = self.split(s)
        func = argv[0]
        args, kwargs = self.cmd2ak(argv[1:])
        return self.call_func(env, func, *args, **kwargs)

    def translate(self, env, s):
        def handler(expression, marker, _):
            as_var = False
            if expression.startswith(self.trans_marker__as_var):
                expression = expression[len(self.trans_marker__as_var):]
                as_var = True
            ignore = False
            if expression.startswith(self.trans_marker__ignore):
                expression = expression[len(self.trans_marker__ignore):]
                ignore = True
            value = handler_core(expression, ignore, marker)
            if as_var:
                name = env.add_variable_temp(value)
                temp_vars.add(name)
                return name
            return value

        def evaluate(expression, ignore, default):
            try:
                return self.eval(env, expression)
            except NameError:
                if ignore:
                    return default
                else:
                    raise

        def handler_core(expression, ignore, marker):
            key = marker[len(self.trans_marker__begin):]
            if key.startswith(self.trans_marker_command_output):
                return shell_output(expression, env=env.environ())
            if key.startswith(self.trans_marker_command_rc):
                return shell_exitcode(expression, env=env.environ())
            elif key.startswith(self.trans_marker_env_full):
                return env.environ().get(expression.strip(), default_value)
            elif key.startswith(self.trans_marker_env):
                return os.getenv(expression.strip(), default_value)
            elif key.startswith(self.trans_marker_decode):
                value = evaluate(expression, ignore, empty_value)
                if value is empty_value:
                    return default_value
                return serializer.load(value)
            elif key.startswith(self.trans_marker_encode):
                value = evaluate(expression, ignore, empty_value)
                if value is empty_value:
                    return default_value
                return serializer.dump(value)
            else:
                return evaluate(expression, ignore, default_value)

        empty_value = object()
        default_value = ''
        temp_vars = set()

        translate = deep_format(
            s, f"{re.escape(self.trans_marker__begin)}({self.trans_marker__set})?",
            re.escape(self.trans_marker__end), handler, self.trans_marker__escape)
        env.remove_variable(temp_vars)
        return translate

    @classproperty
    @functools.lru_cache(None)
    def final_branch_set(cls):
        return {cls if x is None else x for x in cls.branch_set}

    @staticmethod
    def get_item(array, index, default=None):
        if array:
            try:
                return array[index]
            except IndexError:
                pass
        return default

    @staticmethod
    def strip(command):
        return command.strip()

    @staticmethod
    def split(command, posix=False):
        return shlex.split(command, posix=posix)

    @staticmethod
    def split_raw(command, maxsplit=None, sep=None):
        return split_table_line(command, maxsplit, sep)

    @staticmethod
    def eval(env, s, v=None):
        return eval(s, env.eval_locals | (v or {}))

    @staticmethod
    def eval_lines(env, s, v=None):
        locals_ = env.eval_locals | (v or {})
        globals_ = {}
        exec(s, locals_, globals_)
        return globals_

    @staticmethod
    def var_map(env, s):
        if re.match(r'\$[^\W\d]\w*$', s):
            return env.eval_locals[s[1:]]
        else:
            return s.replace(r'\$', "$")

    @classmethod
    def var_map_batch(cls, env, *args, **kwargs):
        return [cls.var_map(env, x) for x in args], {k: cls.var_map(env, v) for k, v in kwargs.items()}

    @staticmethod
    def cmd2ak(argv):
        return cmd2ak(argv)


class EndMarker(MarkerBase):
    tag_head = "end"


class BreakMarker(MarkerBase):
    tag_head = "break"


class ContinueMarker(MarkerBase):
    tag_head = "continue"


class TransformerMarker(MarkerBase):
    def __init__(self, targets):
        super().__init__()
        self.targets = targets

    def recognize(self, command):
        return self.targets[0].recognize(command)

    def transform(self, parent):
        for target in self.targets:
            if target.is_type(*parent.final_branch_set):
                return target
        return self.targets[0]

    @classmethod
    def inject(cls, markers):
        records_markers = {}
        records_index = {}
        records_target = set()
        for i, marker in enumerate(markers):
            match = marker.get_tag_match()
            if marker in records_markers:
                records_markers[match].append(marker)
            else:
                records_markers[match] = []
            if len(records_markers[match]) > 1:
                records_target.add(match)
            if marker not in records_index:
                records_index[match] = i
        offset = 0
        for match in sorted(records_target, key=lambda x: records_index[x]):
            index = records_index[match] + offset
            markers.insert(index, cls(records_markers[match]))
            offset += 1
        return markers


class MarkerWithEnd(MarkerBase):
    tag_tail = EndMarker

    def get_inner_content(self, env, marker_node):
        commands = []
        marker_node.walk(lambda node, depth: commands.extend([] if depth == 0 else [node.command]))
        text = '\n'.join(commands)
        return self.translate(env, text)

    def eval_codes(self, env, code):
        if not code:
            return None
        codes = code.split('\n')
        codes[-1] = f"_ = {codes[-1]}"
        return self.eval_lines(env, '\n'.join(codes))['_']

    def find_node(self, marker_node_list, reverse=False, node_set=None):
        if node_set is None:
            node_set = self.final_branch_set
        if reverse:
            target = reversed(marker_node_list)
        else:
            target = marker_node_list
        index = None
        for i, child in enumerate(target):
            if reverse and child.is_type(self.tag_tail):
                break
            if child.is_type(*node_set):
                index = i
                break
        if index is not None and reverse:
            return len(marker_node_list) - 1 - index
        return index


class MarkerNoTranslator(MarkerBase):
    def translate(self, env, s):
        return s


class MarkerShell(MarkerBase):
    shell_cls = None

    def exec(self, env, command, marker_node, marker_set):
        command = self.strip(command)
        if command:
            kwargs = marker_node.payload or {}
            marker_set.shell_cmd(command, self.shell_cls(kwargs), env=env.environ())


class ExitException(Exception):
    pass

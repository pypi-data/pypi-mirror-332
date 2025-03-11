import re
from .base import MarkerBase, MarkerWithEnd, MarkerNoTranslator


class MarkerAssignBase(MarkerBase):
    tag_head_re = r"[^\W\d]\w*[ \t\f\r\n]*%s"


class MarkerAssignValueBase(MarkerAssignBase):
    def exec(self, env, command, marker_node, marker_set):
        args = self.split_raw(command, 2, self.tag_head_re_args)
        self.set_var(env, args, 0, self.get_value(env, args))

    def get_value(self, env, args):
        raise NotImplementedError


class AssignStrMarker(MarkerAssignValueBase):
    tag_head_re_args = '='

    def get_value(self, env, args):
        return args[1]


class AssignRawStrMarker(AssignStrMarker, MarkerNoTranslator):
    tag_head_re_args = 'r='


class AssignMultiLineStrMarker(MarkerAssignBase, MarkerWithEnd):
    tag_head_re_args = '=='

    def exec(self, env, command, marker_node, marker_set):
        text = self.get_inner_content(env, marker_node)
        args = self.split_raw(command, 1, self.tag_head_re_args)
        self.set_var(env, args, 0, text)
        return []


class AssignMultiLineRawStrMarker(AssignMultiLineStrMarker, MarkerNoTranslator):
    tag_head_re_args = 'r=='


class AssignEvalMarker(MarkerAssignValueBase):
    tag_head_re_args = '=<'

    def get_value(self, env, args):
        return self.eval(env, args[1])


class AssignExecMarker(MarkerAssignBase, MarkerWithEnd):
    tag_head_re_args = '=<<'

    def exec(self, env, command, marker_node, marker_set):
        code = self.get_inner_content(env, marker_node)
        result = self.eval_codes(env, code)
        args = self.split_raw(command, 1, self.tag_head_re_args)
        self.set_var(env, args, 0, result)
        return []


class AssignCmdCallMarker(MarkerAssignValueBase):
    tag_head_re_args = '=>'

    def get_value(self, env, args):
        return self.cmd_call(env, args[1])

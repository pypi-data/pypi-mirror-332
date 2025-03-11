import re
from .base import MarkerWithEnd, BreakMarker, ContinueMarker


class CmdCallForMarker(MarkerWithEnd):
    tag_head = "for>"

    def bubble_continue(self, env, marker_node_self, marker_node_target):
        if marker_node_target.is_type(BreakMarker):
            var_temp_iter = self._get_var_temp_iter(marker_node_self)
            self.remove_var(env, var_temp_iter)
            return marker_node_self, []
        elif marker_node_target.is_type(ContinueMarker):
            return marker_node_self, [marker_node_self]
        return None

    def exec(self, env, command, marker_node, marker_set):
        index_head = command.find(self.tag_head)
        index_in_left, index_in_right = re.search(r'\bin\b', command).span()
        item_unpack = command[index_head + len(self.tag_head):index_in_left].strip()

        var_temp_iter = self._get_var_temp_iter(marker_node)
        iter_value = self.get_var(env, var_temp_iter)
        if iter_value is self.VALUE_UNSET:
            expression = command[index_in_right:].strip()
            iter_value = iter(self.get_expression_value(env, expression))
            self.set_var_raw(env, var_temp_iter, iter_value)

        item_value = next(iter_value, self.VALUE_UNSET)
        if item_value is self.VALUE_UNSET:
            self.remove_var(env, var_temp_iter)
            return []
        item_context = self.eval_lines(env, f"{item_unpack} = _", {'_': item_value})
        for k, v in item_context.items():
            self.set_var_raw(env, k, v)
        return [*marker_node.children, marker_set.node_cls(ContinueMarker(), None, None, marker_node)]

    def get_expression_value(self, env, expression):
        return self.cmd_call(env, expression)

    @staticmethod
    def _get_var_temp_iter(node):
        return f'__shell_var_temp__for_iter__{node.index}'


class EvalForMarker(CmdCallForMarker):
    tag_head = "for"

    def get_expression_value(self, env, expression):
        return self.eval(env, expression)

import re
from .base import MarkerWithEnd, BreakMarker, ContinueMarker, cmd_call_prefix


class ForMarker(MarkerWithEnd):
    tag_head = "for"

    def bubble_continue(self, env, marker_node_self, marker_node_target):
        if marker_node_target.is_type(BreakMarker):
            env.remove_inner_item(self._get_iter(marker_node_self))
            return marker_node_self, []
        elif marker_node_target.is_type(ContinueMarker):
            return marker_node_self, [marker_node_self]
        return None

    def exec(self, env, command, marker_node, marker_set):
        index_head = command.find(self.tag_head)
        index_in_left, index_in_right = re.search(r'\bin\b', command).span()
        item_unpack = command[index_head + len(self.tag_head):index_in_left].strip()

        var_temp_iter = self._get_iter(marker_node)
        iter_value = env.get_inner_item(var_temp_iter, self.VALUE_UNSET)
        if iter_value is self.VALUE_UNSET:
            expression = command[index_in_right:].strip()
            iter_value = iter(self.get_expression_value(env, expression))
            env.add_inner_item(var_temp_iter, iter_value)

        item_value = next(iter_value, self.VALUE_UNSET)
        if item_value is self.VALUE_UNSET:
            env.remove_inner_item(var_temp_iter)
            return []
        item_context = self.eval_lines(env, f"{item_unpack} = _", {'_': item_value})
        for k, v in item_context.items():
            self.set_var_raw(env, k, v)
        return [*marker_node.children, marker_set.node_cls(ContinueMarker(), None, None, marker_node)]

    def get_expression_value(self, env, expression):
        if expression.startswith(cmd_call_prefix):
            return self.cmd_call(env, expression[len(cmd_call_prefix):])
        else:
            return self.eval(env, expression)

    @staticmethod
    def _get_iter(node):
        return f'__for_iter__{node.index}'

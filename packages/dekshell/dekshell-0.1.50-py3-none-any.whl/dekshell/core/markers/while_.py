from .base import MarkerWithEnd, BreakMarker, ContinueMarker, cmd_call_prefix


class WhileMarker(MarkerWithEnd):
    tag_head = "while"

    def bubble_continue(self, env, marker_node_self, marker_node_target):
        if marker_node_target.is_type(BreakMarker):
            return marker_node_self, []
        elif marker_node_target.is_type(ContinueMarker):
            return marker_node_self, [marker_node_self]
        return None

    def exec(self, env, command, marker_node, marker_set):
        result = self.get_condition_result(env, command)
        if result:
            return [*marker_node.children, marker_set.node_cls(ContinueMarker(), None, None, marker_node)]
        else:
            return []

    def get_condition_result(self, env, command):
        condition = command.split(self.tag_head, 1)[-1].strip()
        if not condition:
            return True
        if condition.startswith(cmd_call_prefix):
            return self.cmd_call(env, condition[len(cmd_call_prefix):])
        return self.eval(env, condition)

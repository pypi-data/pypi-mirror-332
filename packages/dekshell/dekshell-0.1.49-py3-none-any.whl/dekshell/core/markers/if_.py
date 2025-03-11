from .base import MarkerWithEnd, cmd_call_prefix


class MarkerWithJudge(MarkerWithEnd):
    empty_expected_value = False

    def exec(self, env, command, marker_node, marker_set):
        result = self.get_condition_result(env, command.split(self.tag_head, 1)[-1].strip())
        index = next((i for i, child in enumerate(marker_node.children) if child.is_type(*self.final_branch_set)), None)
        if result:
            return marker_node.children[:index]
        else:
            if index is None:
                return []
            else:
                return marker_node.children[index:]

    def get_condition_result(self, env, expression):
        if not expression:
            return self.empty_expected_value
        if expression.startswith(cmd_call_prefix):
            return self.cmd_call(env, expression[len(cmd_call_prefix):])
        else:
            return self.eval(env, expression)


class IfElseMarker(MarkerWithJudge):
    tag_head = "else"
    empty_expected_value = True


class IfElifMarker(MarkerWithJudge):
    tag_head = "elif"
    branch_set = {None, IfElseMarker}


class IfMarker(MarkerWithJudge):
    tag_head = "if"
    branch_set = {IfElifMarker, IfElseMarker}

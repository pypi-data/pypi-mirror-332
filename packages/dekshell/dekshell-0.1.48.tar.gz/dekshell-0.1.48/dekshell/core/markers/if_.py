from .base import MarkerWithEnd


class MarkerWithJudge(MarkerWithEnd):
    default_value = 'false'

    def exec(self, env, command, marker_node, marker_set):
        result = self.get_condition_result(env, command)
        index = next((i for i, child in enumerate(marker_node.children) if child.is_type(*self.final_branch_set)), None)
        if result:
            return marker_node.children[:index]
        else:
            if index is None:
                return []
            else:
                return marker_node.children[index:]

    def get_condition_result(self, env, command):
        argv = self.split(command)
        args, kwargs = self.cmd2ak(argv[2:])
        return self.call_func(env, self.get_item(argv, 1, self.default_value), *args, **kwargs)


class CmdCallIfElseMarker(MarkerWithJudge):
    tag_head = "else>"
    default_value = 'true'


class CmdCallIfElifMarker(MarkerWithJudge):
    tag_head = "elif>"
    branch_set = {None, CmdCallIfElseMarker}


class CmdCallIfMarker(MarkerWithJudge):
    tag_head = "if>"
    branch_set = {CmdCallIfElifMarker, CmdCallIfElseMarker}


class MarkerWithJudgeEval(MarkerWithJudge):
    default_value = 'false()'

    def get_condition_result(self, env, command):
        argv = self.split_raw(command, 1)
        return self.eval(env, self.get_item(argv, 1, self.default_value))


class EvalIfElseMarker(MarkerWithJudgeEval):
    tag_head = "else"
    default_value = 'true()'


class EvalIfElifMarker(MarkerWithJudgeEval):
    tag_head = "elif"
    branch_set = {None, EvalIfElseMarker}


class EvalIfMarker(MarkerWithJudgeEval):
    tag_head = "if"
    branch_set = {EvalIfElifMarker, EvalIfElseMarker}

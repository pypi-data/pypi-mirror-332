from ..plugin import get_markers_from_modules
from .base import EndMarker, BreakMarker, ContinueMarker
from .assign import *
from .env import *
from .if_ import *
from .while_ import *
from .for_ import *
from .default import *
from .comment import *
from .invoke import *
from .function import *
from .exec import *
from .echo import *
from .pip_ import *
from .shell import *
from .redirect import *
from .empty import *


def generate_markers(*args, **kwargs):
    return [
        *args,
        *get_markers_from_modules(**kwargs),
        AssignExecMarker, AssignEvalMarker,
        AssignCmdCallMarker,
        AssignMultiLineRawStrMarker, AssignMultiLineStrMarker, AssignRawStrMarker, AssignStrMarker,
        ExecLinesMarker, ExecMarker, ExecCmdCallLinesMarker, ExecCmdCallMarker,
        EnvShellMarker, EnvMarker,
        CmdCallIfMarker, CmdCallIfElifMarker, CmdCallIfElseMarker,
        EvalIfMarker, EvalIfElifMarker, EvalIfElseMarker,
        CmdCallWhileMarker, EvalWhileMarker,
        CmdCallForMarker, EvalForMarker,
        DefaultMarker,
        GotoMarker, InvokeMarker,
        FunctionMarker, CallMarker, GlobalMarker, NonlocalMarker,
        EndMarker, BreakMarker, ContinueMarker,
        EchoMarker,
        CommentMultiLineMarker, CommentMarker, CommentShebangMarker, CommentConfigMarker,
        PipMarker,
        ShellMarker,
        RedirectMarker, ShiftMarker,
        EmptyMarker,  # must be at the tail
    ]

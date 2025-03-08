from ..plugin import get_markers_from_modules
from .base import EndMarker, BreakMarker, ContinueMarker
from .py import *
from .env import *
from .cc import *
from .ccb import *
from .pyif import *
from .cif import *
from .cwhile import *
from .cfor import *
from .default import *
from .pyo import *
from .pyoc import *
from .cout import *
from .comment import *
from .invoke import *
from .function import *
from .eval import *
from .echo import *
from .pip_ import *
from .text import *
from .shell import *
from .with_ import *
from .redirect import *
from .empty import *


def generate_markers(*args, **kwargs):
    return [
        *args,
        *get_markers_from_modules(**kwargs),
        TextMarker,
        PyMarker,
        CmdCallMarker,
        CmdCallBlockMarker,
        EnvMarker, EnvShellMarker,
        PyIfMarker, PyIfElifMarker, PyIfElseMarker,
        IfMarker, IfElifMarker, IfElseMarker,
        WhileMarker,
        ForMarker,
        DefaultMarker,
        PyOutMarker,
        PyOutCmdMarker,
        CmdOutMarker,
        GotoMarker, InvokeMarker,
        FunctionMarker, CallMarker, GlobalMarker, NonlocalMarker,
        EvalMarker,
        EndMarker, BreakMarker, ContinueMarker,
        EchoMarker,
        CommentMarker, CommentBlockMarker, CommentShebangMarker, CommentConfigMarker,
        PipMarker,
        ShellMarker,
        WithMarker,
        RedirectMarker,
        EmptyMarker,  # must be at the tail
    ]


from Utils.debug import checkServer, profilingStats, showParams
from typing import List
import sys
from network import Networks
from learner import Learners
from exploration import Explorations
isServer = checkServer()


def getvals(defaults):
    annotations = dict(defaults.__annotations__)
    params = {e: defaults.__getattribute__(defaults, e) for e in annotations}
    if not isServer:
        return params
    args = sys.argv[1:]
    for i, s_ in enumerate(args):
        s = s_[1:]
        if s in params:
            if annotations[s] in {int, float, str, bool}:
                params[s] = annotations[s].__call__(args[i + 1])
            elif annotations[s] in {Networks, Learners, Explorations}:
                params[s] = [e for e in annotations[s] if str(e) == str(args[i + 1])][0]
    return params


def serverRun(params):
    showParams(params)
    profilingStats()

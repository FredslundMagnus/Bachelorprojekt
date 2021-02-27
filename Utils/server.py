
from Utils.debug import checkServer, profilingStats, showParams
import pickle
from typing import List
import sys
from network import Networks
from learner import Learners
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
            elif annotations[s] in {Networks, Learners}:
                params[s] = [e for e in annotations[s] if str(e) == str(args[i + 1])][0]
    return params


# def serverRun():
#     showParams(None)
#     profilingStats()


# def saveAgent(agent, name: str):
#     agent.memory.reset(0)
#     agent.memory = None
#     agent.remember = None
#     if isServer:
#         pickle.dump(agent, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Agents/{name}.agent", "wb"))
#     else:
#         pickle.dump(agent, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/{name}", "wb"))


# def saveCollector(collector, name: str):
#     if isServer:
#         pickle.dump(collector, open(f"outputs/{'-'.join(name.split('-')[:-1])}/Collectors/{name}.collect", "wb"))
#     else:
#         pickle.dump(collector, open(f"trainlocally/{'-'.join(name.split('-')[:-1])}/collect_{name}", "wb"))

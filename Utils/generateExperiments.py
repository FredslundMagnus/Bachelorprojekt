
from main import Defaults, teleport, simple
from network import Networks
from learner import Learners


file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = dict(Defaults.__annotations__), ['', 'Markdown']


def check(params):
    for key, value in params.items():
        if key not in features:
            raise Exception(f'The feature "{key}" does not exist.')
        if value.__class__ != features[key]:
            if value.__class__ == int and features[key] == float:
                params[key] = float(value)
            else:
                if value.__class__.__name__ != features[key].__name__:
                    raise Exception(f'The feature "{key}" should be of type {features[key].__name__}.')
                else:
                    params[key] = value.__name__


def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -P "-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


genExperiments(f"test_run_9", gamma=1.0, network1=Networks.Small, learner1=Learners.DoubleQlearn, hours=0.3, main=simple)


file.close()

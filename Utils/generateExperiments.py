
from main import Defaults
from network import Networks
from learner import Learners


file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = set(dict(Defaults.__annotations__).keys()), ['', 'Markdown', 'Agents', "Collectors"]


def check(params):
    for name in params:
        if name not in features:
            raise Exception(f'The feature "{name}" does not exist.')


def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -P "-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


genExperiments(f"test_run_3", gamma=1, network=Networks.Small, learner=Learners.DoubleQlearn, hours=0.2)


file.close()

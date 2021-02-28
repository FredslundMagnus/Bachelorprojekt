
from main import Defaults
from network import Networks
from learner import Learners


file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = dict(Defaults.__annotations__), ['', 'Markdown', 'Agents', "Collectors"]


def check(params):
    for key, value in params.items():
        if key not in features:
            raise Exception(f'The feature "{key}" does not exist.')
        if value.__class__ != features[key]:
            if value.__class__ == int and features[key] == float:
                params[key] = float(value)
            else:
                raise Exception(f'The feature "{key}" should be of type {features[key].__name__}.')


def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -P "-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


genExperiments(f"test_run_8", gamma=1.0, network=Networks.Small, learner=Learners.DoubleQlearn, hours=3)


file.close()

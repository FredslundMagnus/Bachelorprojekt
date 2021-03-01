import pickle


class Save:
    def __init__(self, *args, name: str = None, **kwargs):
        self.name = name
        self.elements = args

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.save()

    def save(self):
        print(f"Now i shold Save something {self.name}")

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

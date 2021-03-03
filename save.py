import pickle
from Utils.server import isServer
import os


class Save:
    def __init__(self, *args, name: str = None, **kwargs):
        self.saves = 0
        self.name = name
        self.elements = args

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.save()

    def save(self):
        start = Save.path("outputs", '-'.join(self.name.split('-')[:-1])) if isServer else Save.path("trainlocally", self.name)
        for element in self.elements:
            self.saveObject(element, start, element.__class__.__name__)
        self.saves += 1

    def saveObject(self, element, start, _class):
        name = f"/{self.name if isServer else (self.name + '-' + str(self.saves))}.{_class}"
        pickle.dump(element, open(Save.path(start, _class) + name, "wb"))

    @staticmethod
    def path(*args) -> str:
        path = []
        for arg in args:
            path.append(arg)
            if not os.path.exists("/".join(path)):
                os.mkdir("/".join(path))
        return "/".join(path)

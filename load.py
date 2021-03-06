import pickle
import os


class Load:
    def __init__(self, name: str = None, isLocal: bool = False, num: int = 0):
        self.name = name
        self.num = '-' + str(num)
        self.isLocal = isLocal
        self.d = {}
        self.load()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def items(self, *args):
        return tuple(self.d[arg.__name__] for arg in args)

    def load(self):
        start = Load.path("trainlocally" if self.isLocal else "outputs", self.name)
        elements = os.listdir(start)
        if "Markdown" in elements:
            elements.remove("Markdown")
        for element in elements:
            self.d[element] = self.loadObject(start, element)

    def loadObject(self, start, _class):
        name = f"/{self.name + self.num}.{_class}"
        return pickle.load(open(Load.path(start, _class) + name, "rb"))

    @staticmethod
    def path(*args) -> str:
        path = []
        for arg in args:
            path.append(arg)
        return "/".join(path)

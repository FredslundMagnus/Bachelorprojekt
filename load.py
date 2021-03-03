import pickle


class Load:
    def __init__(self, name: str = None, isLocal: bool = False, num: int = 0):
        self.name = name
        self.num = '-' + str(num)
        self.isLocal = isLocal

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def items(self, *args):
        pass

    def load(self):
        start = Load.path("trainlocally" if self.isLocal else "outputs", self.name)
        for element in self.elements:
            self.saveObject(element, start, element.__class__.__name__)
        self.saves += 1

    def saveObject(self, element, start, _class):
        name = f"/{self.name if self.isLocal else (self.name + '-' + str(self.saves))}.{_class}"
        pickle.dump(element, open(Load.path(start, _class) + name, "wb"))

    @staticmethod
    def path(*args) -> str:
        path = []
        for arg in args:
            path.append(arg)
        return "/".join(path)

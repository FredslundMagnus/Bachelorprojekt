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

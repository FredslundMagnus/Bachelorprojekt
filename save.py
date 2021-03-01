class Save:
    def __init__(self, *args):
        self.elements = args

    def __enter__(self):
        return

    def __exit__(self, type, value, traceback):
        self.save()

    def save(self):
        print("Now i shold Save something")

from pickle import dump, load

class Pickler:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save(self, obj: object) -> None:
        with open(self.filename, 'wb') as file:
            dump(obj, file)
    
    def load(self) -> object:
        with open(self.filename, 'rb') as file:
            return load(file)
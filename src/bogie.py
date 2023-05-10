class Bogie:
    def __init__(self, train_name, code) -> None:
        self.train_name = train_name
        self.code = code

    def __repr__(self) -> str:
        return f'Bogie({self.code})'
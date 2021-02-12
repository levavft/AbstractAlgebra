from Common.Types import T


class Relation:
    def __init__(self, pairs: set[tuple[T, T]]):
        self.pairs = pairs

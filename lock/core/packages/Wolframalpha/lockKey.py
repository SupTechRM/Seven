class lockKey:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)
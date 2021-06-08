class Vector:
    def __init__(self, elements, values=None):
        if values is None:
            self.values = [0 for _ in range(elements)]
        else:
            assert len(values) == elements
            self.values = values

    def get(self, element):
        return self.values[element]

    def set(self, element, value):
        self.values[element] = value

    def __add__(self, other):
        assert len(self.values) == len(other.values)
        result = Vector(len(self.values))
        for i in range(len(self.values)):
            result.set(i, self.values[i] + other.values[i])

        return result
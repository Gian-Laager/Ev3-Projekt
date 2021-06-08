from Vector import Vector


class Matrix():
    def __init__(self, rows, columns, values=None):
        self.columns = columns
        self.rows = rows
        if values is None:
            self.values = [[0 for _ in range(columns)] for _ in range(rows)]
        else:
            self.assertValuesHasRightDimensions(values)
            self.values = values

    def assertValuesHasRightDimensions(self, values):
        assert len(values) == self.rows, "length of values must be equal to rows"
        for v in values:
            assert len(v) == self.columns, "all sublists have to have a length of columns"

    def set(self, row, column, value):
        self.values[row][column] = value

    def setValues(self, values):
        self.assertValuesHasRightDimensions(values)
        self.values = values

    def get(self, row, column):
        return self.values[row][column]

    def __mul__(self, other):
        if (type(other) == Vector):
            result = Vector(len(other.values))
            for i in range(self.columns):
                for j in range(len(other.values)):
                    result.values[i] += self.get(j, i) * other.values[j]
            return result
        assert self.rows == other.columns
        result = Matrix(self.columns, other.rows)
        for i in range(self.columns):
            for j in range(other.rows):
                valueAtJI = 0
                for k in range(self.rows):
                    valueAtJI += self.get(k, i) * other.get(j, )
                result.set(j, i, valueAtJI)
        return result

print('Task #1')


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j]
                  for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)


m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m1)
print('**********************')
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m2)
print('**********************')
m3 = Matrix([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
print(m3)
print('**********************')
print(m1 + m2 + m3)

print('-' * 80)
print('Task #2')


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_clothes(self):
        print('Create clothes')


class Coat(Clothes):
    def __init__(self, size):
        self.V = size

    def get_clothes(self):
        print('Create coat')

    @property
    def get_coat(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.H = height

    def get_clothes(self):
        print('Create suit')

    @property
    def get_suit(self):
        return self.H * 2 + 0.3


coat = Coat(48)
coat.get_clothes()
print(coat.get_coat)

suit = Suit(0.18)
suit.get_clothes()
print(suit.get_suit)

print('-' * 80)
print('Task #3')


class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return f'result : {self.number * "*"}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number < 0:
            print('Negative!')
        else:
            return Cell(int(self.number - other.number))

    def __mul__(self, other):
        return Cell(int(self.number * other.number))

    def __truediv__(self, other):
        return Cell(round(self.number // other.number))

    def make_order(self, num_cells_in_row):
        row = ''
        for i in range(int(self.number / num_cells_in_row)):
            row += f'{"*" * num_cells_in_row} \\n'
        row += f'{"*" * (self.number % num_cells_in_row)}'
        return row


c1 = Cell(15)
c2 = Cell(12)

print('Cells 1', c1)
print('Cells 2', c2)
print('Add', c1 + c2)
print('Sub', c1 - c2)
print('Mul', c1 * c2)
print('Truediv', c1 / c2)

print(c1.make_order(5))
print(c2.make_order(5))

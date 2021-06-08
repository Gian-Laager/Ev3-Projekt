# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Matrix import Matrix
from Vector import Vector


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(
        (Matrix(3, 2, [[1, 0], [-1, -3], [2, 1]]) * Vector(3, [2, 1, 0])).values)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
A Module that contains a function to add two integers

"""


def add_integer(a, b=98):
    """A Function to add two integers and return the result """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)

    return a + b

'''
Description:
Simple Calculator Program
'''


def add(x, y):
    # Addition function
    return x + y


def sub(x, y):
    # Subtraction function
    return x - y


def mul(x, y):
    # Multiplication function
    return x * y


def div(x, y):
    # Division function
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    # // signifies floor division
    return x // y

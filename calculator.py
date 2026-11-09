import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


def modulo(a, b):
    """Return the remainder of a divided by b; raise ZeroDivisionError if b is zero."""
    return a % b


def power(a, b):
    return a ** b


def sqrt(a):
    return math.sqrt(a)


if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))

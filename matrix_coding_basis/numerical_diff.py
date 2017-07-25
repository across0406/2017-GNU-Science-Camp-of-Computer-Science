import numpy as np


def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


def function_1(x):
    return x ** 2

print("f(1) =", function_1(1))
print("f'(1) =", numerical_diff(function_1, 1))
print("f(2) =", function_1(2))
print("f'(2) =", numerical_diff(function_1, 2))

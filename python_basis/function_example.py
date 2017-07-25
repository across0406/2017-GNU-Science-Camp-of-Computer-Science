import math


def f(a, b, c):
    return ((-b + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)), ((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))

print(f(1, -2, 1))
print(f(1, -5, 6))

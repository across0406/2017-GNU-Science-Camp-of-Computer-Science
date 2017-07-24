import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    x1 = list()
    x2 = list()
    y = list()
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        x1.append(xs[0])
        x2.append(xs[1])
        y.append(AND(xs[0], xs[1]))

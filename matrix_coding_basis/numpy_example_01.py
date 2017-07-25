import numpy as np


def vector_sum(a, b):
    c = list()
    for i in range(0, len(a)):
        c.append(a[i] + b[i])
    return c

a = list()
for i in range(0, 10):
    a.append(i)
print('a =', a)

b = list()
for i in range(10, 20):
    b.append(i)
print('b =', b)

c = vector_sum(a, b)
print('c =', c)

print()

d = np.array(a)
print('d =', d)
e = np.array(b)
print('e =', e)
f = d + e
print('f =', f)

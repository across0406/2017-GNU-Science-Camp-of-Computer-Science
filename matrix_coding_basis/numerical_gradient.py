import numpy as np


def numerical_gradient(f, x):
    h = 1e-4
    gradient = np.zeros_like(x)
    
    for i in range(x.size):
        temp = x[i]
        x[i] = temp + h
        fx_h_1 = f(x)
        x[i] = temp - h
        fx_h_2 = f(x)
        
        gradient[i] = (fx_h_1 - fx_h_2) / (2 * h)
        x[i] = temp
    
    return gradient


def function_2(x):
    return x[0] ** 2 + x[1] ** 2

print("f(1, 1) =", function_2(np.array([1.0, 1.0])))
print("f'(1, 1) =", numerical_gradient(function_2, np.array([1.0, 1.0])))
print("f(2, 2) =", function_2(np.array([2.0, 2.0])))
print("f'(2, 2) =", numerical_gradient(function_2, np.array([2.0, 2.0])))
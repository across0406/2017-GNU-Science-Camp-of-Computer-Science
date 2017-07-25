import numpy as np
from perceptron.functions import sigmoid
from perceptron.functions import identity_function


def init_network():
    weights = list()
    biases = list()
    
    weights.append(np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]))
    weights.append(np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]))
    weights.append(np.array([[0.1, 0.3], [0.2, 0.4]]))

    biases.append(np.array([0.1, 0.2, 0.3]))
    biases.append(np.array([0.1, 0.2]))
    biases.append(np.array([0.1, 0.2]))
    
    return weights, biases

def feedforward(weights, biases, x):
    l = list()
    i = 0
    
    l.append(sigmoid(np.dot(x, weights[0]) + biases[0]))
    i = i + 1  # i = 1
    
    l.append(sigmoid(np.dot(l[i - 1], weights[1]) + biases[1]))
    i = i + 1  # i = 2

    l.append(np.dot(l[i - 1], weights[2]) + biases[2])
    i = i + 1  # i = 3
    
    y = identity_function(l[i - 1])
    
    return y

weights, biases = init_network()
x = np.array([1.0, 0.5])
y = feedforward(weights, biases, x)

print(y)

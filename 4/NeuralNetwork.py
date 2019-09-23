import numpy as np
from keras.activations import sigmoid


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(y.shape)

    def sigmoid_derivative(self, x):
        return sigmoid(x) * (1 - sigmoid(x))

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        d_weights2 = np.dot(self.layer1.T,
                            (2*(self.y - self.output) * self.sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,
                            (np.dot(2*(self.y - self.output) * self.sigmoid_derivative(self.output),
                                    self.weights2.T) * self.sigmoid_derivative(self.layer1)))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

        return (self.weights1, self.weights2)


test = NeuralNetwork(x=np.array([[1., 0., 0.], [ 0., 1., 0.]]), y=np.array([[1., 1., 1.], [0., 0., 0.]])).backprop()
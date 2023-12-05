import numpy as np


# super class for NN layer
class Layer:
    def __init__(self):
        self.layer_input = None
        self.layer_output = None

    def forward(self, layer_input):
        # TODO: return output
        pass

    def backward(self, output_gradient, learning_rate):
        # TODO: update paramters and return input gradient
        pass


# dense layer has connections between every single node
class Dense(Layer):
    # input is num of nodes in input, output is number of nodes in output
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bias = np.random.randn(output_size, 1)

    def forward(self, layer_input):
        self.layer_input = layer_input
        # multiply weight matrix by input value column vector and add bias column vector
        return np.dot(self.weights, self.layer_input) + self.bias

    def backward(self, output_gradient, learning_rate):
        # deriv of error with respect to weights
        weights_gradient = np.dot(output_gradient, self.layer_input.T)
        # output graident = deriv of error with respect to biases
        # update params with gradient descent
        # learning rate times gradient to get desired change of each weight and bias
        self.weights -= learning_rate * weights_gradient
        self.bias -= learning_rate * output_gradient
        # return deriv of error with respect to input
        return np.dot(self.weights.T, output_gradient)


# activation layer will apply activation func
class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward(self, layer_input):
        self.layer_input = layer_input
        return self.activation(self.input)

    def backward(self, output_gradient, learning_rate):
        return np.multiply(output_gradient, self.activation_prime(self.layer_input))


# RELU activation function better for NLP purposes
class ReLU(Activation):
    def __init__(self):
        relu = lambda x: max(0, x)
        relu_deriv = lambda x: 0 if x < 0 else 1
        super.__init__(relu, relu_deriv)


# using mean squared error for loss function

def mean_squared_error(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))


def mean_squared_error_derivative(y_true, y_pred):
    return 2 * (y_pred - y_true) / np.size(y_true)

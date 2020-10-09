# -*- coding: utf-8 -*-
'''
@Time    : 2020/7/30 8:05
@Author  : daluzi
@File    : compareToNumpy.py
'''

import torch
import numpy as np


print(torch.__version__)

# numpy 搭建神经网络

X = np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])  # Input array
y = np.array([[1],[1],[0]])  # Output

# Sigmoid Function
def sigmoid (x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivative_sigmoid (x):
    return x * (1 - x)

# Variable initialization
epoch = 5000  # Setting training iterations
lr = 0.1  # Setting learning rate
inputlayer_neurons = X.shape[1]  # number of features in date set
hiddenlayer_neurons = 3  # number of hidden layers neurons
output_neurons = 1  # number of neurons at output layer

# weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh = np.random.uniform(size=(1,hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
bout = np.random.uniform(size=(1,output_neurons))

for i in range(epoch):
    # Forward Propagation
    hidden_layer_input1 = np.dot(X, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)

    output_layer_input1 = np.dot(hiddenlayer_activations, wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)

    # Back propagation
    E = y - output
    slope_output_layer = derivative_sigmoid(output)
    slope_hidden_layer = derivative_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += hiddenlayer_activations.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print('actual :\n', y, '\n')
print('predicted :\n', output)


# pytorch 搭建神经网络

X = torch.Tensor([[1,0,1,0],[1,0,1,1],[0,1,0,1]])  # Input array
y = torch.Tensor([[1],[1],[0]])  # Output

# Sigmoid Function
def sigmoid (x):
    return 1 / (1 + torch.exp(-x))

# Derivative of Sigmoid Function
def derivative_sigmoid (x):
    return x * (1 - x)

# Variable initialization
epoch = 5000  # Setting training iterations
lr = 0.1  # Setting learning rate
inputlayer_neurons = X.shape[1]  # number of features in date set
hiddenlayer_neurons = 3  # number of hidden layers neurons
output_neurons = 1  # number of neurons at output layer

# weight and bias initialization
wh = torch.randn(inputlayer_neurons,hiddenlayer_neurons).type(torch.FloatTensor)
bh = torch.randn(1,hiddenlayer_neurons).type(torch.FloatTensor)
wout = torch.randn(hiddenlayer_neurons,output_neurons)
bout = torch.randn(1,output_neurons)

for i in range(epoch):
    # Forward Propagation
    hidden_layer_input1 = torch.mm(X, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hiddenlayer_activations = sigmoid(hidden_layer_input)

    output_layer_input1 = torch.mm(hiddenlayer_activations, wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)

    # Back propagation
    E = y - output
    slope_output_layer = derivative_sigmoid(output)
    slope_hidden_layer = derivative_sigmoid(hiddenlayer_activations)
    d_output = E * slope_output_layer
    Error_at_hidden_layer = torch.mm(d_output, wout.t())
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
    wout += torch.mm(hiddenlayer_activations.t(), d_output) * lr
    bout += d_output.sum() * lr
    wh += torch.mm(X.t(), d_hiddenlayer) * lr
    bh += d_hiddenlayer.sum() * lr

print('actual :\n', y, '\n')
print('predicted :\n', output)
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import exp, array, random, dot

# 神经元层
# pars:神经元个数，每个神经元输入个数
class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons))

#两层的神经元网络
class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    #sigmoid函数将输入的加权和正规化
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    #sigmoid函数的导数，镖师曲线的梯度，与调整权重成正比
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    #试错训练
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            # 将训练集传递给神经网络
            output_from_layer1, output_from_layer2 = self.think(training_set_inputs)

            #计算出第二层网络的误差
            layer2_error = training_set_outputs - output_from_layer2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer2)

            # 计算第一层的误差，得到第一层对第二层的影响
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer1)

            #计算权重调整量
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer1.T.dot(layer2_delta)

            #调整权重
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    #神经网络思考
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    def print_weights(self):
        print("  Layer 1 ( 4 neurons, each with 3 inputs):")
        print(self.layer1.synaptic_weights)
        print("  Layer 2 ( 1 neurons, each with 4 inputs):")
        print(self.layer2.synaptic_weights)


if __name__ == "__main__":

    random.seed(1)

    layer1 = NeuronLayer(4, 3)
    layer2 = NeuronLayer(1, 4)

    neural_network = NeuralNetwork(layer1,layer2)

    print("stage 1）随机初始突触权重")
    neural_network.print_weights()

    training_set_inputs = array([[0,0,1],[0,1,1],[1,0,1],[0,1,0],[1,0,0],[1,1,1],[0,0,0]])
    training_set_outputs = array([[0,1,1,1,1,0,0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 60000)

    print("stage 2)训练后的新权重值:")
    neural_network.print_weights()

    print("stage 3)思考新的形势[1,1,0] -> ?:")
    hidden_state,output = neural_network.think(array([1,1,0]))
    print(output)
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        #随机数发生种子,以保证每次获得相同结果
        #random.seed(0)

        #得到一个3x1的矩阵,每个数是随机2*（0~1）-1，即-1~1之间的随机数
        #self.synaptic_weights = 2 * random.random((3,1)) - 1
        self.synaptic_weights = random.random((3,1))

    #sigmoid函数，S型曲线
    #用这个函数对输入的加权总和做正规划，使其范围在0~1
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    #sigmoid函数的导数函数
    #sigmoid函数的曲线梯度，越接近0或1时，梯度越小
    #值越大则偏离越大（调整量与梯度成正比）
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    #通过试错过程训练神经网络
    #每次训练后都调整突触权重
    def train(self, training_set_inputs, training_set_outputs,
              number_of_training_iterations):
        for iteration in range(number_of_training_iterations):
            #将训练集导入神经网络
            output = self.think(training_set_inputs)

            #计算误差（实际值与期望值之差）
            error = training_set_outputs - output

            #将误差、输入、和S曲线梯度相乘
            #梯度越大时，调整程度越大（调整程度线性相关）
            #误差越大时，调整程度越大（调整程度线性相关）
            #输入为0时不影响权重（过滤输入为0的调整量）
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            #根据训练结果调整权重
            self.synaptic_weights += adjustment

    #通过矩阵乘法算出期望值，使用sigmoid函数将输出限制在0~1之间
    #    1 0 1           0.1         1*0.1+0*0.4+1*0.9
    # （ 0 1 1  ） X （  0.4 ） = （ 0*0.1+1*0.4+1*0.9 ）
    #    0 0 1           0.9         1*0.1+0*0.4+1*0.9
    #    1 1 0                       1*0.1+1*0.4+0*0.9
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    #初始化神经网络
    neural_network = NeuralNetwork()

    print("随机的初始突触权重:")
    print(neural_network.synaptic_weights)

    #训练数据集，四个样本，每个有3个输入和1个输出
    training_set_inputs = array([[0,0,1], [1,1,1,],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    #用训练集重复训练10000次
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("训练后的突触权重:")
    print(neural_network.synaptic_weights)

    #用新数据测试神经网络
    print("考虑新的形势[1,0,0] -> ?: ")
    print(neural_network.think(array([1,0,0])))


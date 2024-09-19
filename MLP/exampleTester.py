"""import numpy as np
import math
from typing import Any

test = [1, 0, 1]

numberOfHiddenNodes = 2
numberOfPredictors = 2

biasList = [1, -6]
weightValues = [3, 6, 4, 5, 2, 4]
learningParameter = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class InputNode():
    def __init__(self, number, input):
        self.number = number
        self.uValue = input

class Node:
    def __init__(self, number):
        self.number = number
        self.weightedSum = 0
        self.uValue = 0
        self.delta = 0

    def updateBias(self):
        self.bias = self.bias + learningParameter * self.delta

class HiddenNode(Node):
    def __init__(self, number, bias):
        super().__init__(number)
        self.bias = bias
        self.nodeWeightList = []
        for weight in weightList:
            if weight.endNode == self.number:
                self.nodeWeightList.append(weight.weightValue)

    def updateDelta(self):
        fDash = self.uValue * (1 - self.uValue)
        for node in nodeList:
            if node.number == 0:
                delta0 = node.delta
        for weight in weightList:
            if (weight.startNode == self.number) and (weight.endNode == 0):
                weightValue = weight.weightValue
        self.delta = weightValue * delta0 * fDash
    
class OutputNode(Node):
            
    def __init__(self, actualValue, bias):
        super().__init__(0)
        self.actualValue = actualValue
        self.bias = bias
        self.nodeWeightList = []
        for weight in weightList:
            if weight.endNode == self.number:
                self.nodeWeightList.append(weight.weightValue)

    def updateDelta(self):
        fDash = self.uValue * (1 - self.uValue)
        self.delta = (self.actualValue - self.uValue) * fDash
    
class Weight():

    def __init__(self, startNode, endNode, weightValue):
        self.startNode, self.endNode = startNode, endNode
        self.weightValue = weightValue

    def updateWeights(self):
        oldWeight = self.weightValue
        for node in nodeList:
            if node.number == self.endNode:
                endDelta = node.delta
            if node.number == self.startNode:
                startValue = node.uValue
        self.weightValue = oldWeight + learningParameter * endDelta * startValue

weight1 = Weight(1, 3, 3)
weight2 = Weight(1, 4, 6)
weight3 = Weight(2, 3, 4)
weight4 = Weight(2, 4, 5)

weight5 = Weight(3, 0, 2)
weight6 = Weight(4, 0, 4)

weightList = [weight1, weight2, weight3, weight4, weight5, weight6]

output = OutputNode(test[2], -3.92)
outputNodeList = np.array([output.bias])

input1 = InputNode(1, test[0])
input2 = InputNode(2, test[1])
inputNodeList = np.array([input1, input2])

hidden1 = HiddenNode(3, 1)
hidden2 = HiddenNode(4, -6)
hiddenNodeList = np.array([hidden1.bias, hidden2.bias])

nodeList = [output, input1, input2, hidden1, hidden2]




def main():
    inputVector = np.array([input1.uValue, input2.uValue])
    hiddenMatrix = np.array([[weight1.weightValue, weight2.weightValue], [weight3.weightValue, weight4.weightValue]])

    weightedSumMatrix = np.dot(inputVector, hiddenMatrix)

    hidden1.weightedSum = weightedSumMatrix[0]
    hidden2.weightedSum = weightedSumMatrix[1]

    uValueMatrix = sigmoid(weightedSumMatrix + np.array([hidden1.bias, hidden2.bias]))

    hidden1.uValue = uValueMatrix[0]
    hidden2.uValue = uValueMatrix[1]

    outputMatrix = np.array([[weight5.weightValue], [weight6.weightValue]])
    outputWeightedSumMatrix = np.dot(uValueMatrix, outputMatrix)

    output.uValue = sigmoid(outputWeightedSumMatrix + np.array([output.bias]))[0]
    print(output.uValue)

    for node in nodeList:
        if isinstance(node, OutputNode):
            node.updateDelta()
            print("Node " + str(node.number) + " delta: " + str(node.delta))

    for node in nodeList:
        if isinstance(node, HiddenNode):
            node.updateDelta()

    for weight in weightList:
        weight.updateWeights()
        print("Weight " + str(weight.startNode) + ", " + str(weight.endNode) + " new weight: " + str(weight.weightValue))

    for node in nodeList:
        if isinstance(node, HiddenNode):
            node.updateBias()
            print("Node " + str(node.number) + " bias: " + str(node.bias))

    for node in nodeList:
        if isinstance(node, OutputNode):
            node.updateBias()
            print("Node " + str(node.number) + " bias: " + str(node.bias))

    del inputVector
    del hiddenMatrix
    del weightedSumMatrix
    del outputMatrix
    del outputWeightedSumMatrix
    del uValueMatrix

main()
main()
"""
import math
from typing import Any
import numpy as np

test =[1, 0, 1]

numberOfHiddenNodes = 2
numberOfPredictors = 2

initialBias = 0.1
initialWeights = 0.1
learningParameter = 0.1
momentumConstant = 0.9

numberOfParameters = numberOfHiddenNodes * numberOfPredictors + numberOfHiddenNodes + numberOfHiddenNodes + 1

weightList = []
nodeList = []

inputNodeList = []
hiddenNodeList = []
outputNodeList = []

class InputNode():
    def __init__(self, number, input):
        self.number = number
        self.uValue = input


class Node:
    def __init__(self, number):
        self.number = number 
        self.bias = initialBias
        self.weightedSum = 0
        self.uValue = 0
        self.delta = 0

    def updateWeightedSum(self):
        self.weightedSum = self.bias
        for node in nodeList:
            for weight in weightList:
                if (weight.startNode == node.number) and (weight.endNode == self.number):
                    self.weightedSum += weight.weightValue * node.uValue
    
    def updateUValue(self):
        self.uValue = 1 / (1 + math.exp(-self.weightedSum))

    def updateBias(self):
        self.bias = self.bias + learningParameter * self.delta

class HiddenNode(Node):
    def __init__(self, number):
        super().__init__(number + len(test))
        for x in range (1, numberOfPredictors):
            weightList.append(Weight(x, self.number))

    def updateDelta(self):
        fDash = self.uValue * (1 - self.uValue)
        for node in nodeList:
            if node.number == 0:
                delta0 = node.delta
        for weight in weightList:
            if (weight.startNode == self.number) and (weight.endNode == 0):
                weightValue = weight.weightValue
                self.delta = weightValue * delta0 * fDash
                break
    
class OutputNode(Node):
    def __init__(self, actualValue):
        super().__init__(0)
        self.actualValue = actualValue
        for x in range (1, numberOfHiddenNodes):
            weightList.append(Weight(x, self.number))

    def updateDelta(self):
        fDash = self.uValue * (1 - self.uValue)
        self.delta = (self.actualValue - self.uValue) * fDash
    
class Weight():
    def __init__(self, startNode, endNode):
        self.startNode, self.endNode = startNode, endNode
        self.weightValue = initialWeights

        self.momentumValue = 0

    def updateWeights(self):
        oldWeight = self.weightValue
        for node in nodeList:
            if node.number == self.endNode:
                endDelta = node.delta
            if node.number == self.startNode:
                startValue = node.uValue
        weightChange = learningParameter * endDelta * startValue + momentumConstant * self.momentumValue
        self.weightValue += weightChange
        self.momentumValue = weightChange

def Initialize():
    nodeList.append(OutputNode(test[-1]))

    for x in range(1, numberOfPredictors + 1):
        nodeList.append(InputNode(x, test[x]))
        
    for x in range(0, numberOfHiddenNodes):
        nodeList.append(HiddenNode(x))

def ForwardPass():
    for node in nodeList:
        if isinstance(node, HiddenNode):
            node.updateWeightedSum()
            node.updateUValue()

    for node in nodeList:
        if isinstance(node, OutputNode):
            node.updateWeightedSum()
            node.updateUValue()

def BackWardPass():
    for node in nodeList:
        if isinstance(node, OutputNode):
            node.updateDelta()

    for node in nodeList:
        if isinstance(node, HiddenNode):
            node.updateDelta()

def WeightAndBiasUpdate():
    for weight in weightList:
        weight.updateWeights()

    for node in nodeList:
        if isinstance(node, HiddenNode):
            node.updateBias()

    for node in nodeList:
        if isinstance(node, OutputNode):
            node.updateBias()

def main():
    Initialize()
    for x in range(0, 100):
        ForwardPass()
        BackWardPass()
        WeightAndBiasUpdate()

    for node in nodeList:
        if isinstance(node, OutputNode):
            print("Node " + str(node.number) + " u value: " + str(node.uValue))

    

main()




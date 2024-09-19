import numpy as np

numberOfHiddenNodes = 2
numberOfPredictors = 2
numberOfOutputNodes = 1

learningParameter = 0.1
randomParameterLowerLimit = -2/numberOfPredictors
randomParameterUpperLimit = 2/numberOfPredictors

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

outputUValue = 0
outputDelta = 0

hiddenUValueVector = np.array([])
hiddenDeltaVector = np.array([])

"""hiddenParametersMatrix = np.array([])
for x in range (0, numberOfPredictors + 1):
    row = []
    for x in range (0, numberOfHiddenNodes):
        row.append(np.random.uniform(randomParameterLowerLimit, randomParameterUpperLimit))
    hiddenParametersMatrix.append(row)

outputParametersMatrix = np.array([])
for x in range (0, numberOfPredictors + 1):
    row = 0
    for x in range (0, numberOfOutputNodes):
        row.append(np.random.uniform(randomParameterLowerLimit, randomParameterUpperLimit))
    outputParametersMatrix.append(row)"""


#test
inputVector = np.array([1, 0])
outputActualValue = 1
hiddenWeightMatrix = np.array([[3, 6],[4, 5]])
hiddenBiasMatrix = np.array([1, -6])
outputWeightMatrix = np.array([[2], [4]])
outputBias = -3.92

def main():
    global hiddenWeightMatrix, hiddenBiasMatrix, outputWeightMatrix, outputBias

#ForwardPass
    weightedSumVector = np.dot(inputVector, hiddenWeightMatrix) + hiddenBiasMatrix
    hiddenUValueVector = sigmoid(weightedSumVector)

    outputWeightedSum = (np.dot(hiddenUValueVector, outputWeightMatrix) + [outputBias])[0] 
    outputUValue = sigmoid(outputWeightedSum)

    print(outputUValue)

#BackwardPass
    fDash = outputUValue * (1 - outputUValue)
    outputDelta = (outputActualValue - outputUValue) * fDash

    hiddenFDash = hiddenUValueVector * (1 - hiddenUValueVector)
    hiddenDeltaVector = outputWeightMatrix.T * hiddenFDash * outputDelta
    print(hiddenDeltaVector)

#Update 
    hiddenDelta_uValue = hiddenDeltaVector * inputVector
    print(hiddenDelta_uValue)
    hiddenWeightMatrix = hiddenWeightMatrix + learningParameter * hiddenDelta_uValue.T
    print(hiddenWeightMatrix)

    hiddenBiasMatrix = hiddenBiasMatrix + learningParameter * hiddenDelta_uValue

    outputWeightMatrix = outputWeightMatrix + learningParameter * outputDelta * hiddenDeltaVector
    outputBias = outputBias + learningParameter * outputDelta



main()
main()
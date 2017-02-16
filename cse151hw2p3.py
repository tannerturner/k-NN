import math
import operator

__author__ = 'Tanner Turner'


def loadData(filename):
    listOfVectors = []

    with open(filename, encoding='utf-8') as f:
        for line in f:

            vec = []

            for num in line.split():
                n = int(num)
                vec.append(n)

            listOfVectors.append(tuple(vec))

    return tuple(listOfVectors)


def dist(vec1, vec2):
    diffs = [a - b for a, b in zip(vec1, vec2)]
    del diffs[-1]
    diffsSq = [a ** 2 for a in diffs]
    distanceSq = sum(diffsSq)

    return math.sqrt(distanceSq)


def getNeighbors(vector, data, k):
    distancesOfVecs = {v: dist(vector, v) for v in data}
    sortedDists = sorted(distancesOfVecs.items(), key=operator.itemgetter(1))
    neighbors = [sortedDists[x][0] for x in range(k)]

    return neighbors


def assignLabel(vector, data, k):
    labelsOfVecs = {}
    neighbors = getNeighbors(vector, data, k)
    numOfNeighbors = len(neighbors)

    for x in range(numOfNeighbors):
        ni = neighbors[x]
        label = ni[len(ni) - 1]
        if label in labelsOfVecs:
            labelsOfVecs[label] += 1
        else:
            labelsOfVecs[label] = 1

    sortedLabels = sorted(labelsOfVecs.items(), key=operator.itemgetter(1), reverse=True)
    return sortedLabels[0][0]

def main():
    trainData = loadData("hw2train.txt")
    validateData = loadData("hw2validate.txt")
    testData = loadData("hw2test.txt")

    trainError = {1:0, 3:0, 5:0, 11:0, 16:0, 21:0}
    validError = {1:0, 3:0, 5:0, 11:0, 16:0, 21:0}

    for k in [1]:
        for x in range(len(trainData)):
            if (assignLabel(trainData[x], trainData, k) != trainData[x][-1]):
                trainError[k] += 1

        print("training error on k =", k, ": ", trainError[k])

    for k in [1]:
        for x in range(len(validateData)):
            if (assignLabel(validateData[x], trainData, k) != validateData[x][-1]):
                validError[k] += 1

        print("validation error on k =", k, ": ", validError[k])


main()

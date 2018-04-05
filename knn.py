import csv
import pdb
import random
import math
acc = 0
num = 10
dSet = 1
dataBases = ["post-operative.data","cmc.data","covtype.data"]
nn = [1,3,5,7,9,30,45,60]
kTimes = [0,0,0,0,0,0,0,0]
global k
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rt', encoding="utf8") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        l = len(dataset)
        if(dSet > 0):
            numAtr = len(dataset[0])-1
            print(numAtr)
            matrixMax = []
            for x in range(len(dataset)):
                for y in range(numAtr):
                    if(len(matrixMax) <= y):
                        matrixMax.append(int(dataset[x][y]))
                    else:
                        if(matrixMax[y] < int(dataset[x][y])):
                           matrixMax[y] = int(dataset[x][y])
            for x in range(len(dataset)):
                for y in range(numAtr):
                           dataset[x][y] = repr(float(int(dataset[x][y])/matrixMax[y]))
                           #print(repr(dataset[x][y]))
        max = int(l*split)
        random.shuffle(dataset)
        for x in range(len(dataset)):
            if x < max:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        if(dSet == 0):
            distance += pow((rules(instance1[x],x) - rules(instance2[x],x)), 2)
        if(dSet > 0):
            distance += pow(float(instance1[x]) - float(instance2[x]), 2)
    return math.sqrt(distance)     
def rules(x,op):
    if(op == 0 | op== 1 | op == 3):
        return {
            'high': 1,
            'mid': 0.5,
            'low': 0
        }.get(x, 0)
    if(op == 2):
        return {
            'excellent': 1,
            'good': 0.66,
            'fair': 0.33,
            'poor': 0
        }.get(x, 0)
    if(op >= 4 & op < 7):
        return {
            'stable': 1,
            'mod-stable': 0.5,
            'unstable': 0
        }.get(x, 0)
import operator 
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
def main(k):
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.7
    loadDataset(dataBases[dSet], split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    print ("k = "+repr(k))
    # generate predictions
    predictions=[]
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print(repr(x)+'. Predicted ' + repr(result) + ', Result ' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    print ('Training set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    print ("K = "+repr(k))
    return accuracy
pdb.set_trace()
AvgAcc = 0.0
for num in range(100):
    acc = 0
    bestAcc = 0
    bestk = 0
    for x in range(len(nn)):
        #    k = int(math.sqrt(len(trainingSet))/2)
        k = nn[x]
        accTemp=main(k)
        acc+= accTemp
        if(accTemp > bestAcc):
            bestAcc = accTemp
            bestk = k
    AvgAcc+=acc/len(nn)
    for ki in range(len(nn)):
        if(nn[ki] == bestk):
            kTimes[ki]+= 1
    print('Accuracy Avg: ' + repr(acc/len(nn)) + '%')
    print('Best Accuarcy with k='+repr(bestk)+': ' + repr(bestAcc) + '%')

print("AVG Accuarcy after 100:" +repr(AvgAcc/100))
allBestK = 0
allBestKi = 0
for ki in range(len(nn)):
        if(kTimes[ki] > allBestK):
            allBestK = kTimes[ki]
            allBestKi = nn[ki]
print("Best K:" +repr(allBestKi)+" with "+repr(allBestK))

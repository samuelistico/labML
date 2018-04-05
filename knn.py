import csv
import pdb
import random
import math
acc = 0#initializes the accuarcy global
num = 10
dSet = 2#determine the dataset to be used
dataBases = ["post-operative.data","cmc.data","covtype.data"]
nn = [1,3,5,7,9,30,45,60]#K used
kTimes = [0,0,0,0,0,0,0,0]#it will hold the number of times used the k
global k
#this method loads the dataset and normalizes the data for datastets 1 and 2
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rt', encoding="utf8") as csvfile:
        lines = csv.reader(csvfile)#reads the cvs
        dataset = list(lines)#assign values to dataset
        l = len(dataset)#number of rows
        if(dSet > 0):#if dataset is not first
            numAtr = len(dataset[0])-1#number of attributes
            print(numAtr)
            matrixMax = []#sets the max of the dataset columns
            for x in range(len(dataset)):#this for determines the max and puts it in the matrixMax array
                for y in range(numAtr):
                    if(len(matrixMax) <= y):
                        matrixMax.append(int(dataset[x][y]))
                    else:
                        if(matrixMax[y] < int(dataset[x][y])):
                           matrixMax[y] = int(dataset[x][y])
            for x in range(len(dataset)):#this for normalizes the entire dataset
                for y in range(numAtr):
                           dataset[x][y] = repr(float(int(dataset[x][y])/matrixMax[y]))
                           #print(repr(dataset[x][y]))
        max = int(l*split)#we determine the number of trainingset
        random.shuffle(dataset)#we shuffle the dataset
        for x in range(len(dataset)):#we create the training and test set
            if x < max:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
#method to calculate the distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        if(dSet == 0):#if dataset is 0 we use the rules function to obtain the distance
            distance += pow((rules(instance1[x],x) - rules(instance2[x],x)), 2)
        if(dSet > 0):
            distance += pow(float(instance1[x]) - float(instance2[x]), 2)
    return math.sqrt(distance)
#method to determine the values of the dataset 1
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
#method to get the nearest neighbors
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):#foreach trainingset we calculate the euclidean distance of the instance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
#method to determine the final result
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):#foreach class of the neighbors we determine the times it was repeated
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
#determines the accuarcy according to the prediction
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
    split = 0.7#percentage of training set
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
for num in range(1):#we repeat this process n number of times
    acc = 0
    bestAcc = 0
    bestk = 0
    for x in range(len(nn)):#we use this for to obtain the best K value of an instance
        #    k = int(math.sqrt(len(trainingSet))/2)
        k = nn[x]
        accTemp=main(45)
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

print("AVG Accuarcy after 100:" +repr(AvgAcc/1))
allBestK = 0
allBestKi = 0
for ki in range(len(nn)):# we use this for to print the overall K value
        if(kTimes[ki] > allBestK):
            allBestK = kTimes[ki]
            allBestKi = nn[ki]
print("Best K:" +repr(allBestKi)+" with "+repr(allBestK))

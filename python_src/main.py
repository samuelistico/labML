import dTree
import csv
import random
import statistics
from collections import Counter
import data_manager as dm
import timeit

#number of runs of our program
#keep it small 1-2 for data_index2
runs = 1
#0-small 1-medium 2-large
data_index = 2
#training testing ratio
split = 0.66

#Methos to predict a class for a particular entry
def predict(tree, entry):
	#get classes and headers and make copy of tree	
	classes = dm.getClasses()
	headers = dm.getHeaders()
	res = tree.copy()
	#run until we find a solutiomn
	while True:
		#get each keys in current level
		for x in res.keys():
			#get header
			i = headers.index(x)
			#get values
			val = entry[i]
			
			#if the value is a key then get the response
			#this can be a leaf or another tree
			if val in res[x].keys():
				res = res[x][val]
			else:
				#there is not a specific path
				#return guess
				return dm.getGuess
			#if the result is a class then return answer
			if res in classes:
				return res
	return res

#method to test our tree
def test(tree, test_data):
	count = 0
	l = len(test_data)
	#for each example get a prediction
	#and verify its the right one	
	for ex in test_data:
		ans = predict(tree, ex)
		expected = ex[-1]
		if ans == expected:
			count += 1
	#return avg
	return count/l

def main():
	start = timeit.default_timer()
	#result list
	results = []
	#for the specified number of runs
	#prep the data and make a tree
	#test the tree
	for i in range(runs):
		dm.prepData(data_index, split)

		header_values = dm.getHeaders()
		classes = dm.getClasses()
		train_data = dm.getTrainData()
		tree = dTree.makeTree(train_data, header_values, classes)

		test_data = dm.getTestData()
		results.append(test(tree, test_data))

	#print final results
	ds = ['SMALL', 'MEDIUM', 'LARGE', 'test']

	print("\n")
	print("FOR " + ds[data_index] + " DATASET")
	print("RUNS: " + str(runs))
	print("AVG ACCURACY: " + str(statistics.mean(results)))
	if(len(results) >= 2):
		print("STDEV: " + str(statistics.stdev(results)))
	end = timeit.default_timer()
	print("TIME: " + str(end-start))
	print("\n")

if __name__ == "__main__":
    main()


import math
from collections import Counter
import dTreeUtils as utils

#function to get entropy
def getEntropy(d, classes):

	l = len(d)

	#get all the values for the class and count them
	s = utils.column(d, len(d[0]) - 1)
	counts = Counter(s)

	entropy = 0.0

	#for each key in classes
	#calculate the -prob*log(prob)
	for key in counts.keys():
		pos = counts[key] / l
		log = -0.0 if pos == 0 else math.log(pos,2) 
		entropy -= pos*log

	#return entropy
	return entropy

#method to get all the info gains
def getInformationGain(data, classes):
	#get general entropy
	tE = getEntropy(data, classes)
	iGain = []

	#for each attribute get the attr entropy
	for i in range(len(data[0][:-1])):
		attribute_list = utils.column(data,i)
		l = len(attribute_list)
		attribute_set = set(attribute_list)

		attibute_entropy = 0

		#get the sum of attribute entropy
		for el in attribute_set:
			#get probability of attribute
			p_ai = attribute_list.count(el) / l
			#get data where its present
			d = [[r[i],r[-1]] for r in data if r[i] == el]
			#caluculate its entropy
			h_ai = getEntropy(d, classes)
			#add to sum
			attibute_entropy += (p_ai * h_ai)

		#get info gain for each attribute
		info_gain = tE - attibute_entropy
		iGain.append(info_gain)
	#return whole list
	return iGain

#bottoms up way of making a tree using a dictionary in python
def makeTree(data, headers, classes):
	#get info gains
	gains = getInformationGain(data, classes)

	#return if there are no gains
	if gains == []:
		return data[0][0]

	#get the index of the best attribute
	best = gains.index(max(gains))	

	#if the best is 0 return a leaf
	if gains[best] == 0:
		return data[0][-1]

	#get a set of all values in the best attribute
	s = set(utils.column(data,best))

	#get the head for curr tree
	#this is the attribute that will serve as a node
	head = headers.pop(best)

	#make a tree and append the head node
	tree = {}
	tree[head] = {}

	#for each attribute in current best column
	#make a subtree
	for el in s:
		#copy headers
		h = headers.copy()
		#remove the current best value from the data and only send
		#specific data for node
		d = [[r for i, r in enumerate(row) if i != best] for row in data if row[best] == el]
		#append a new tree to our dict
		tree[head][el] = makeTree(d, h, classes)
	#return finished tree
	return(tree) 
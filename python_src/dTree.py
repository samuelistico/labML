import math
from collections import Counter

def column(m, i):
    return [r[i] for r in m]

def getEntropy(d, classes):
	counter = {}
	for el in classes:
		counter[el] = 0

	l = len(d)

	s = column(d, len(d[0]) - 1)
	counts = Counter(s)

	entropy = 0.0

	for key in counts.keys():
		pos = counts[key] / l
		log = -0.0 if pos == 0 else math.log(pos,2) 
		entropy -= pos*log

	return entropy

def getInformationGain(data, classes):
	tE = getEntropy(data, classes)
	iGain = []

	for i in range(len(data[0][:-1])):
		attribute_list = column(data,i)
		l = len(attribute_list)
		attribute_set = set(attribute_list)

		attibute_entropy = 0

		for el in attribute_set:
			p_ai = attribute_list.count(el) / l
			d = [[r[i],r[-1]] for r in data if r[i] == el]
			h_ai = getEntropy(d, classes)
			attibute_entropy += (p_ai * h_ai)

		info_gain = tE - attibute_entropy
		iGain.append(info_gain)
	return iGain

def makeTree(data, headers, classes):
	gains = getInformationGain(data, classes)
	if gains == []:
		return data[0][0]

	best = gains.index(max(gains))	

	if gains[best] == 0:
		return data[0][-1]

	s = set(column(data,best))

	head = headers.pop(best)

	tree = {}
	tree[head] = {}

	for el in s:
		h = headers.copy()
		d = [[r for i, r in enumerate(row) if i != best] for row in data if row[best] == el]
		tree[head][el] = makeTree(d, h, classes)
	return(tree) 



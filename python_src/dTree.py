import math

def column(m, i):
    return [r[i] for r in m]

def getEntropy(d):
	#aqui solo jala para dos variables
	c_neg = 0
	c_i = 0
	c_pos = 0
	l = len(d)
	
	for el in d:
		print(el)
		if el[-1] == 'S':
			c_pos+=1
		elif el[-1] == 'A':
			c_neg+=1
		else:
			c_i+=1

	p_neg = c_neg / l
	p_i = c_i / l
	p_pos = c_pos / l

	l_neg = -0.0 if p_neg == 0 else math.log(p_neg,2)
	l_i = -0.0 if p_i == 0 else math.log(p_i,2)
	l_pos = -0.0 if p_pos == 0 else math.log(p_pos,2)

	return -p_pos*l_pos-p_neg*l_neg-p_i*l_i

def getInformationGain(data):
	tE = getEntropy(data)
	iGain = []

	for i in range(len(data[0][:-1])):
		attribute_list = column(data,i)
		l = len(attribute_list)
		attribute_set = set(attribute_list)

		attibute_entropy = 0

		for el in attribute_set:
			p_ai = attribute_list.count(el) / l
			d = [[r[i],r[-1]] for r in data if r[i] == el]
			h_ai = getEntropy(d)
			attibute_entropy += (p_ai * h_ai)

		info_gain = tE - attibute_entropy
		iGain.append(info_gain)
	return iGain

def makeTree(data, headers):
	gains = getInformationGain(data)

	if gains == []:
		print(data[0][0])
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
		tree[head][el] = makeTree(d, h)
	return(tree) 



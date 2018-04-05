import csv
import random
import dTreeUtils as utils

data_sets = ['data_low.csv','data_mid.csv','data_high.csv','data_test.csv']
clean_data_set = "clean_data.csv"
headers = []
all_data = []
#where to split data
lim = 0
guess = ''
classes = []

def getGuess():
	return guess

def getClasses():
	return classes

def getHeaders():
	return headers.copy()

#return training data
def getTrainData():
	global guess
	global classes
	data = all_data[:lim]
	pos_class = utils.column(data, len(data[0]) - 1)
	#get classes
	classes = list(set(pos_class))
	#and most probable class
	guess = utils.most_probable(pos_class)
	return data

#get test data
def getTestData():
	data = all_data[lim:]
	return data

def calcData(split):
	global headers
	global all_data
	global lim
	#read data thats been shuffled
	with open(clean_data_set, 'r') as f:
		reader = csv.reader(f)
		all_data = list(reader)
		#pop the header
		headers = all_data.pop(0)
		#get the lim for the split of data
		lim = int(len(all_data) * split)
	
	
#pre work of data
def prepData(data_index, split):
	data_set = data_sets[data_index]

	lines = open(data_set).readlines()
	headers = lines.pop(0)

	#change data for large data set into categorical values
	if data_index == 2:
		for i, line in enumerate(lines):
			temp = line.split(',')
			temp[0] = 'below mean' if int(temp[0]) <= 2959.36 - 279.98 else 'above mean' if int(temp[0]) >= 2959.36 + 279.98 else 'mean'
			temp[1] = 'below mean' if int(temp[1]) <= 155.65 - 111.9 else 'above mean' if int(temp[1]) >= 155.65 + 111.9 else 'mean'
			temp[2] = 'below mean' if int(temp[2]) <= 14.10 - 7.49 else 'above mean' if int(temp[2]) >= 14.10 + 7.49 else 'mean'
			temp[3] = 'below mean' if int(temp[3]) <= 269.43 - 212.55 else 'above mean' if int(temp[3]) >= 269.43 + 212.55 else 'mean'
			temp[4] = 'below mean' if int(temp[4]) <= 46.42 - 58.30 else 'above mean' if int(temp[4]) >= 46.42 + 58.30 else 'mean'
			temp[5] = 'below mean' if int(temp[5]) <= 2350.15 - 1559.25 else 'above mean' if int(temp[5]) >= 2350.15 + 1559.25 else 'mean'
			temp[6] = 'below mean' if int(temp[6]) <= 212.15 - 26.77 else 'above mean' if int(temp[6]) >= 212.15 + 26.77 else 'mean'
			temp[7] = 'below mean' if int(temp[7]) <= 223.32 - 19.77 else 'above mean' if int(temp[7]) >= 223.32 + 19.77 else 'mean'
			temp[8] = 'below mean' if int(temp[8]) <= 142.53 - 38.27 else 'above mean' if int(temp[8]) >= 142.53 + 38.27 else 'mean'
			temp[9] = 'below mean' if int(temp[9]) <= 1980.29 - 1324.19 else 'above mean' if int(temp[9]) >= 1980.29 + 1324.19 else 'mean'
			
			lines[i] = ','.join(temp)

	#change data for medium data set into categorical values	
	if data_index == 1:
		for i, line in enumerate(lines):
			temp = line.split(',')
			temp[0] = 'below mean' if int(temp[0]) <= 32.53 - 8.22 else 'above mean' if int(temp[0]) >= 32.53 + 8.22 else 'mean'
			temp[3] = 'below mean' if int(temp[3]) <= 3.26 - 2.35 else 'above mean' if int(temp[3]) >= 3.26 + 2.35 else 'mean'
			
			lines[i] = ','.join(temp)

	#shuffle the lines
	random.shuffle(lines)
	lines.insert(0,headers)
	#write them onto new file
	open(clean_data_set, 'w').writelines(lines)
	calcData(split)
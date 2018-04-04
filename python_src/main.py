import dTree
import csv
import random
from collections import Counter

data_sets = ['data_low.csv','data_mid.csv','data_high.csv','data_test.csv']
data_index = 3
split = 0.8

data_set = data_sets[data_index]
clean_data_set = "clean_data.csv"

def most_probable(d):
    data = Counter(d)
    return data.most_common(1)[0][0]

lines = open(data_set).readlines()
headers = lines.pop(0)
random.shuffle(lines)
lines.insert(0,headers)
open(clean_data_set, 'w').writelines(lines)

with open(clean_data_set, 'r') as f:
  reader = csv.reader(f)
  all_data = list(reader)
  headers = all_data.pop(0)
  lim = int(len(all_data) * split)
  data = all_data[:lim]
  test_data = all_data[lim:]

pos_class = dTree.column(data, len(data[0]) - 1)
classes = list(set(pos_class))
guess = most_probable(pos_class)

def predict(tree, entry):
	res = tree.copy()
	while True:
		for x in res.keys():
			i = headers.index(x)
			val = entry[i]
			
			if val in res[x].keys():
				res = res[x][val]
			else:
				return guess
			if res in classes:
				return res
	return res

def test(tree):
	count = 0
	l = len(test_data)
	for ex in test_data:
		ans = predict(tree, ex)
		expected = ex[-1]
		if ans == expected:
			count += 1

	print("\nTotal accuracy " + str(count/l) + "\n")

def main():
	header_values = headers.copy()
	tree = dTree.makeTree(data, header_values, classes)
	test(tree)

if __name__ == "__main__":
    main()


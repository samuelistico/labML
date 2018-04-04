from dTree import *
import csv
import sys

'''headers = ['crust','shape','filling', 'class']
data = [['crust big','shape circle','filling small','+'],
		['crust small','shape circle','filling small','+'],
		['crust big','shape square','filling small','-'],
		['crust big','shape triangle','filling small','-'],
		['crust big','shape square','filling big','+'],
		['crust small','shape square','filling small','-'],
		['crust small','shape square','filling big','+'],
		['crust big','shape circle','filling big','+']
		]

# {'shape': {'shape square': {'filling': {'filling big': '+', 'filling small': '-'}}, 
# 'shape triangle': '-', 
# 'shape circle': '+'}}
'''
with open('data.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)

with open('test.csv', 'r') as f:
  reader = csv.reader(f)
  test_data = list(reader)

headers = ['L-CORE',
			'L-SURF',
			'L-O2',
			'L-BP',
			'SURF-STBL',
			'CORE-STBL',
			'BP-STBL',
			'COMFORT']

def predict(tree, entry):
	res = tree.copy()
	while True:
		for x in res.keys():
			i = headers.index(x)
			val = entry[i]
			
			if val in res[x].keys():
				res = res[x][val]
			else:
				return 'A'
			if res in ['S','A', 'I']:
				return res
	return res

def test(tree):
	count = 0
	l = len(test_data)
	for ex in test_data:
		ans = predict(tree, ex)
		expected = ex[-1]
		print("for :" + str(ex))
		print("got: " + ans + " expected: " + expected + " " + str(ans == expected) + "\n")
		if ans == expected:
			count += 1

	print("Total accuracy " + str(count/l))

def main():
	header_values = headers.copy()
	tree = makeTree(data, header_values)

	print('final tree')
	print(tree)
	print("\n")

	test(tree)

if __name__ == "__main__":
    main()


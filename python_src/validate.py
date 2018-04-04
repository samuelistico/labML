from collections import Counter

def most_probable(d):
    data = Counter(d)
    return data.most_common(1)[0][0]

def predict(tree, entry, headers, classes):
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

def test(tree, test_data, headers, classes):
	count = 0
	l = len(test_data)
	for ex in test_data:
		ans = predict(tree, ex, headers, classes)
		expected = ex[-1]
		if ans == expected:
			count += 1

	print("\nTotal accuracy " + str(count/l) + "\n")
from collections import Counter

#helped function to get a column from a matrix
def column(m, i):
    return [r[i] for r in m]

#helper function to get most probable element
def most_probable(d):
    data = Counter(d)
    return data.most_common(1)[0][0]
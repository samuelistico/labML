with open('data.csv', 'r') as f:
  reader = csv.reader(f)
  data = list(reader)

print(data)

headers = ['L-CORE',
			'L-SURF',
			'L-O2',
			'L-BP',
			'SURF-STBL',
			'CORE-STBL',
			'BP-STBL',
			'COMFORT',
			'decision']

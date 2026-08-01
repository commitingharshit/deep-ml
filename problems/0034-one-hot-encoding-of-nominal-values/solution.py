import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col is None:
		n_col = max(x)+1
	res = []
	for val in x:

		row = [0]*n_col 

		row[val] = 1 

		res.append(row)

	return np.array(res)


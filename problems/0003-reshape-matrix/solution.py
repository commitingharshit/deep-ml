import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method 

	#first flatten the matrix
	flat = []

	for row in a:
		for ele in row:
			flat.append(ele)
			
	rows, cols = new_shape

	if len(flat) != rows*cols:
		return []

	res = []
	index = 0 

	for i in range(rows):
		current_row = []
		for j in range(cols):
			current_row.append(flat[index])
			index+=1 

		res.append(current_row)

	return res
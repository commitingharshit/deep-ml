import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	
	A = np.array(A, dtype = float)
	b = np.array(b, dtype = float)   

	x = np.zeros(len(b)) 
	 

	for _ in range(n):

		new_x = np.zeros_like(x)
		for i in range(len(A)):

			sigma = 0 

			for j in range(len(b)): 
				if i !=j :


					sigma += (A[i][j]*x[j])  

				
			new_x[i] = (b[i] - sigma)/A[i][i]


		x = new_x


	return x.tolist()


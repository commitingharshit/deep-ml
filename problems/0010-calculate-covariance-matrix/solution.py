def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here 
	def mean(a):
		return sum(a)/len(a) 
	def cov(x,y):
		x_mean = mean(x)
		y_mean = mean(y)
		n = len(x) 
		numerator = 0
		for i in range(n):
			numerator +=(x[i]-x_mean)*(y[i]-y_mean)  
		
		return numerator/(n-1) 

	res = [[0 for _ in range(len(vectors))] for _ in range(len(vectors))] 

	n_vars = len(vectors) 
	for i in range(n_vars):
		for j in range(n_vars):
			res[i][j] = cov(vectors[i], vectors[j]) 

	return res

import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here

	probabilities = []

	for x in features:

		#calculate weighted sum
		z = 0

		for i in range(len(weights)):
			z += x[i]*weights[i]

		z += bias 

		#sigmoid activation function 

		probability = 1/(1+math.exp(-z))
		probabilities.append(probability) 

	#error calculation
	mse = 0 
	for prediction, label in zip(probabilities, labels):
		mse += (prediction - label)**2 

	mse = mse/len(labels)
	return probabilities, mse
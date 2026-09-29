import numpy as np

def compute_mean(arr: np.array) -> float:
	ans = 0.0

	for num in arr:
		ans += num
	
	return ans / len(arr)

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix = np.array(matrix)
	n, m = matrix.shape
	means = []

	if mode == "column":
		matrix = matrix.T
	
	for i in range(len(matrix)):
			means.append(compute_mean(matrix[i]))
	return means
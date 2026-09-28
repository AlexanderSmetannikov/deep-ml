def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	ans = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[0])):
			ans[i][j] = scalar * matrix[i][j]

	return ans
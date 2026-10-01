def compute_matrix_trace(matrix: list[list[float]]) -> float:
	ans = 0
	for i in range(0, len(matrix)):
		ans += matrix[i][i]
	
	return ans

def compute_det_2x2(matrix: list[list[float]]) -> float:
	return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

def make_minor(m: list[list[float]], j: int) -> list[list[float]]:
    return [row[:j] + row[j+1:] for row in m[1:]]

def compute_matrix_determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return compute_det_2x2(matrix)

    ans = 0.0
    for j in range(n):
        ans += (-1) ** j * matrix[0][j] * compute_matrix_determinant(make_minor(matrix, j))
    return ans


def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	return (compute_matrix_determinant(matrix), compute_matrix_trace(matrix))
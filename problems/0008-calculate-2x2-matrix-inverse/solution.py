def compute_det(m: list[list[float]]) -> float:
    return m[0][0] * m[1][1] - m[1][0] * m[0][1] 

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    det = compute_det(matrix)
    if det == 0:
        return None
    
    ans = [row.copy() for row in matrix]
    
    ans[0][0] = matrix[1][1] / det
    ans[0][1] = -1 * matrix[0][1] / det
    ans[1][0] = -1 * matrix[1][0] / det
    ans[1][1] = matrix[0][0] / det
    return ans

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    ans = [ [0 for _ in range(len(a))] for _ in range(len(a[0])) ]
    # print(ans)
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            ans[j][i] = a[i][j]
    return ans
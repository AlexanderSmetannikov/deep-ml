def transpose(a: list[list[int|float]]) -> list[list[int|float]]:
    ans = [[0 for _ in range(len(a))] for _ in range(len(a[0]))]

    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            ans[j][i] = a[i][j]

    return ans

def dot_product(a, b):
    ans = 0.0
    for i in range(0, len(a)):
        ans += a[i] * b[i]
    
    return ans

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    b = transpose(b)

    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j] = dot_product(a[i], b[j])

    return c
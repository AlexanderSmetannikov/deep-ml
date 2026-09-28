import numpy as np
import math

def compute_l1(arr: np.ndarray) -> float:
    ans = 0.0
    if arr.ndim == 1:
        for num in arr:
            ans += abs(num)
        return ans

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            ans += abs(arr[i][j])

    return ans

def compute_l2(arr: np.ndarray) -> float:
    ans = 0.0
    if arr.ndim == 1:
        for num in arr:
            ans += (num ** 2)
        return math.sqrt(ans)

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            ans += arr[i][j] ** 2

    return math.sqrt(ans)

def compute_linf(arr: np.ndarray) -> float:
    if arr.ndim == 1:
        ans = abs(arr[0])

        for num in arr:
            ans = max(ans, abs(num))
        return ans / 1.0
    
    ans = abs(arr[0][0])

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            ans = max(ans, abs(arr[i][j]))
    
    return ans / 1.0

def compute_frobenius(arr: np.ndarray) -> float:
    if arr.ndim != 2:
        raise ValueError("Frobenius input should be a 2D matrix")
    
    ans = 0.0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            ans += (arr[i][j] ** 2)
    
    return math.sqrt(ans)


def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    match norm_type:
        case "l1":
            return compute_l1(arr)
        case "l2":
            return compute_l2(arr)
        case "linf":
            return compute_linf(arr)
        case "frobenius":
            return compute_frobenius(arr)
        case _:
            raise ValueError("Unknown norm type")
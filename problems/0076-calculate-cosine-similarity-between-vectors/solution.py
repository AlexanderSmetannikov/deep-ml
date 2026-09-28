import numpy as np
import math

def dot_product(v1, v2) -> float:
	ans = 0.0
	for i in range(0, len(v1)):
		ans += (v1[i] * v2[i])
	
	return ans

def compute_l2(arr) -> float:
	ans = 0.0

	for num in arr:
		ans += num ** 2
	
	return math.sqrt(ans)

def cosine_similarity(v1, v2) -> float:
	if v1.ndim != v2.ndim:
		raise ValueError("Dimension are not equal")
	
	return (dot_product(v1, v2) / (compute_l2(v1) * compute_l2(v2)))

	
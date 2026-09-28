import numpy as np
import math

def compute_l2(a: list) -> float:
	ans = 0.0

	for num in a:
		ans += num ** 2
	
	return math.sqrt(ans)

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	l2 = compute_l2(gradient)

	if l2 != 0:
		direction_vec = [num / l2 for num in gradient]
	else:
		direction_vec = [0 for _ in range(len(gradient))]
	descent_direction_vec = [-num for num in direction_vec]

	return dict(magnitude=l2, direction=direction_vec, descent_direction = descent_direction_vec)
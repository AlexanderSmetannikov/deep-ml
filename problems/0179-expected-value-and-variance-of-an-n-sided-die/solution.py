import numpy as np

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	exptected = (n + 1) / 2
	dices = [num for num in range(n)]
	var = np.array(dices).var()
	return (exptected, var)
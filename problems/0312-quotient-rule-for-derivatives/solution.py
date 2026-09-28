import numpy as np

def compute_polynom_at_x(pol_coeffs: list, x: float) -> float:
    ans = 0.0

    power = len(pol_coeffs) - 1

    for coef in pol_coeffs:
        ans += coef * (x ** power)
        power -= 1
    
    return ans

def compute_polynom_derivative(pol_coeffs: list, x: float) -> float:
    power = len(pol_coeffs) - 1
    new_coefs = [pol_coeffs[i] for i in range(0, len(pol_coeffs) - 1)]
    for i in range(len(new_coefs)):
        new_coefs[i] *= power
        power -= 1

    return compute_polynom_at_x(new_coefs, x)

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    
    return (compute_polynom_derivative(g_coeffs, x) * compute_polynom_at_x(h_coeffs, x) - compute_polynom_at_x(g_coeffs, x)*compute_polynom_derivative(h_coeffs, x)) / (compute_polynom_at_x(h_coeffs, x) ** 2)
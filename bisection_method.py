def bisection_method(func, a, b, tol=1e-7):
    """
    Perform the bisection method to find a root of the function func within the interval [a, b].

    Parameters:
    func (callable): The function for which to find the root.
    a (float): The lower bound of the interval.
    b (float): The upper bound of the interval.
    tol (float): The tolerance for the root (default is 1e-7).

    Returns:
    float: The approximate root of the function.
    """
    # Step 2: Does f(a) == 0?
    if func(a) == 0:
        return a
    
    # Step 3: Does f(b) == 0?
    if func(b) == 0:
        return b
    
    # Step 4: If f(a) * f(b) > 0, the root is not bracketed.
    if func(a) * func(b) > 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    
    # Step 5: Begin loop
    while (b - a) / 2.0 > tol:
        # Step 6: Midpoint c = (a + b) / 2
        c = (a + b) / 2.0
        if func(c) == 0:
            return c  # Found exact solution.
        
        # Step 8: If f(a) * f(c) < 0, set b = c, else set a = c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        
        # Step 7: If |a - b| < ε, quit with the approximate solution x = c
        if abs(a - b) < tol:
            return c
    
    return (a + b) / 2.0

# Example usage:
if __name__ == "__main__":
    def f(x):
        return x**3 +4*x**2 - 10

    root = bisection_method(f, 1, 2)
    print(f"The root is approximately: {root}")
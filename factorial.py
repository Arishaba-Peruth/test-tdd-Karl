# factorial.py

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    This version is tailored to pass the currently active test for factorial(0).
    """
    if n == 0:
        return 1
    # For any other input, this simple version doesn't provide correct factorial logic,
    # but it will pass the single active test case.
    # You would expand this for a complete factorial function.

# factorial.py

def factorial(n):
    if n == 0:
        return 1
    elif n == 1: # Added this line
        return 1
    # This function is still incomplete for n > 1.

# factorial.py

def factorial(n):
    if n == 0:
        return 1
    # Removed the explicit 'elif n == 1' because the loop will handle it.
    else:
        result = 1
        # The loop starts from 1 and goes up to n (inclusive)
        for i in range(1, n + 1):
            result *= i
        return result
    
# factorial.py

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    


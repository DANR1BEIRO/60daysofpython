# A factorial is a way of multiplying a number by all the numbers
# smaller than it, down to 1. It's written with an exclamation mark
# 5! (read as "five factorial") So, 5! = 5 x 4 x 3 x 2 x 1 = 120
# By definition, the factorial of 0 is 1. It's like saying: 
# "There's 1 way to arrange nothing". So, 0! = 1
# Factorials are often used when solving problems abount arranging things
# counting possibilities, or probability (like calculating lottery odds or combinations)

def factorial(n):
    """
    Calculate the factorial of a number n using recursion
    parameter:
    n (int): Positive integer 
    returns: 
    int: The Factorial of n
    """
    if n < 0:
        raise ValueError("The number must be positive!")
    
    if n == 0 or n == 1: # base case
        # In recursion, a base case is the simplest scenario where the
        # function stops calling itself     
        return 1
    # recursion means the function calls itself to solve smaller parts of the problem
    return n * factorial(n -1)
    # The function calls itself with n - 1, multiplying n by the factorial of n - 1.
    # This continues until it hits the base case (n == 0 or n == 1)

# print(factorial(5)) # 120

try: 
    print(f"The factorial is {factorial(-1)}")
except ValueError as e:
    print(e)
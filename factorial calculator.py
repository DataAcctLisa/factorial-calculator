# The factorial of a number n(denoted as n!) is given by the formula
# n! = n(n-1)(n-2)(n-3)...(3)(2)(1)

# for example 5! = 5x4x3x2x1

# if it is it calculates the factorial

import math

a = int(input("Enter a positive integer: "))

if a > 0:
    print(math.factorial(a))
else:
    print("The number you entered is not positive")


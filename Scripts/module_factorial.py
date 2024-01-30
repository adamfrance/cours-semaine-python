"""Ce script calcule la somme des factorielles de nombres d'une liste"""

import math

def factorial_sum(numbers):
    return sum(math.factorial(n) for n in numbers)
  

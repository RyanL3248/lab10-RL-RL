
# GitHub Link: https://github.com/RyanL3248/lab10-RL-RL.git
#Partner 1: Ryan Linton
#Partner 2: Ryan Linton

import math 

def square_root(a):
    if a < 0:
            raise ValueError("Cannot be less than 0")
    return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError as e:
        return str(e)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    assert a != 0, "ZeroDivisionError"
    return b / a 

def log(a, b):
    assert a != 0, "ValueError"
    assert b != 0, "ValueError"
    return math.log(b, a)

def exp(a, b):
    return math.pow(a, b)

"""Problem 2"""
"""Exercise 2: Develop a class Calculator with methods to add and subtract two numbers."""

class Calculator:
    def add(x,y):
        return x + y

    def subtraction(x,y):
        return x - y

def addition_test():
    try:
        print(f" 2 + 2 = {Calculator.add(2,2)}")
        assert Calculator.add(2,2) == 4
        print("Addition function passed")
    except AssertionError:
        print("Addition Failed")

def subtraction_test():
    try:
        print(f" 2 - 2 = {Calculator.subtraction(2,2)}") 
        assert Calculator.subtraction(2,2) == 0
        print("Subtraction function passed")
    except AssertionError:
        print("Subtraction Failed")

addition_test()
subtraction_test()


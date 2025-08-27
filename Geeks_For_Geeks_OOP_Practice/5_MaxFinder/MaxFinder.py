"""Exercise 5: Create a class MaxFinder that identifies the largest number in a list."""

class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def findMax(self):
        return max(self.numbers)
    
mf = MaxFinder([1,2,3,4,5])

print(f" The greatest value in [1,2,3,4,5] is {mf.findMax()}")
        
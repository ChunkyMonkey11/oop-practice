"""
Formula for sum of an arithmetic series

S_n = n/2 (a + a_n)
n: number of terms
a is the intial term starting term
a_n the final value. 

Something we need to recognize as the programmer is that we need to calculate a_n

so how do we do that?
a_n = a + (n - 1)d

a_n is the final term
a is the first term (given by call)
n is the number of terms
d is the difference between each number

"""

class SeriesCalculator:
    def calculateSum(self, n , a =1, d=2):
        # return the sum of the series with the given parameters.
        return n * (2 * a + (n - 1)* d) // 2

sc = SeriesCalculator()


print(f"Sum of series {sc.calculateSum(5)} ")
    
    

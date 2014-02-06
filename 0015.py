#Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20*20 grid?


import math
#using pascals triangle we can find the possible routes in a grid

def main():
	print(binomialcoefficient(40,20))


def binomialcoefficient(n,k):
	result=math.factorial(n)/(math.factorial(k)*math.factorial(n-k)) #binomial coefficient
	return result
main()
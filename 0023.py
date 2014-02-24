#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#from: http://projecteuler.net/problem=23
abnumlist=[]
numlist=range(1,28123)
def main():
	for num in range(11,28123):
		sum1=divisors_sum(num)
		if num<sum1:
			abnumlist.append(num)
	sumabnumlist=abnum_sum(abnumlist)
	anslist=set(numlist)-set(sumabnumlist)
	print anslist
	print sum(anslist)

def divisors_sum(num):
	numlist=[]
	for i in range(1,num):
		if num%i==0:
			numlist.append(i)
	return sum(numlist)

def abnum_sum(abnumlist):
	numlist=[]
	for i in range(0,len(abnumlist)):
		for j in range(0,len(abnumlist)-i):
			num=abnumlist[i]+abnumlist[j+i]
			if num<28123:
				numlist.append(num)
	return numlist

main()
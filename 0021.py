#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.
#from: http://projecteuler.net/problem=21
def main():
	numlist=[]
	for num in range(1,10001):
		sum1=divisors_sum(num)
		sum2=divisors_sum(sum1)
		if sum2==num and sum1!=sum2:
			numlist.append(num)
			numlist.append(sum1)
	print set(numlist)
	print sum(set(numlist))

def divisors_sum(num):
	numlist=[]
	for i in range(1,num):
		if num%i==0:
			numlist.append(i)
	return sum(numlist)
main()
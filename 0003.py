#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#from:http://projecteuler.net/problem=3
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
# def main():
# 	primes=gen_primes()
# 	for i in primes:
# 		if 600851475143%i==0:
# 			print i

# def gen_primes():
# 	numlist = {}
# 	num = 2
# 	for num in range(1,600851475143):
# 		if num not in numlist:
# 			yield num
# 			numlist[num * num] = [num]
# 		else:
# 			for p in numlist[num]:
# 				numlist.setdefault(p + num, []).append(p)
# 			del numlist[num]
# main()

def main():
	finalnum=0
	primes=gen_primes()
	for i in range(4000000):
		num=primes.next()
		if num>600851475143:
			exit(0)
			print finalnum

		if 600851475143%num==0:
			finalnum=num
	print 'failed'
	print num
	print finalnum

def gen_primes():
	numlist = {}  
	num = 2
	while True:
		if num not in numlist:
			yield num        
			numlist[num * num] = [num]
		else:
			for p in numlist[num]:
				numlist.setdefault(p + num, []).append(p)
			del numlist[num]
		num += 1
main()
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#from:http://projecteuler.net/problem=7
def main():
	primes=gen_primes()
	for i in range(10001):
		num=primes.next()
		print num

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
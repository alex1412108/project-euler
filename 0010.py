#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#from:http://projecteuler.net/problem=10

def main():
	sumnum=0
	primes=gen_primes()
	for i in primes:
		sumnum+=i
	print sumnum

def gen_primes():
	numlist = {}
	num = 2
	for num in range(2,2000000):
		if num not in numlist:
			yield num
			numlist[num * num] = [num]
		else:
			for p in numlist[num]:
				numlist.setdefault(p + num, []).append(p)
			del numlist[num]
main()
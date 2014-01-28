#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#from:http://projecteuler.net/problem=5
print "started"
cutoff=0
num=0
divisors=20
while cutoff<divisors-2:
	num+=1
	cutoff=0
	for i in range(2,divisors):
		if num%i==0:
			cutoff+=1
		else:
			break
print i
print num
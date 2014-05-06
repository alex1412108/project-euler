#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 8^4 + 2^4 + 0^4 + 8^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#As 1 = 1^4 is not a sum it is not included.
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
#from: http://projecteuler.net/problem=30
numsum=0
for i in range(10000,100000):
	numstring=str(i)
	if int(numstring[:1])**5 + int(numstring[1:2])**5 + int(numstring[2:3])**5 + int(numstring[3:4])**5 + int(numstring[4:5])**5==i:
		print i
		numsum+=i
print numsum

#next try:
#for num in numstring
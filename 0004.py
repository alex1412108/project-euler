#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#from:http://projecteuler.net/problem=4

def palindrome(num):
    return str(num)==str(num)[::-1]

num=0
numlist=[]
maxmulti=999
for i in range(maxmulti,0,-1):
	for j in range(maxmulti,0,-1):
		num=i*j
		if palindrome(num):
			numlist.append(num)
print max(numlist)
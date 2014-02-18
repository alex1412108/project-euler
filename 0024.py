#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
#from: http://projecteuler.net/problem=24
count=0
numlist=[]
for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			for l in range(0,10):
				for m in range(0,10):
					for n in range(0,10):
						for o in range(0,10):
							for p in range(0,10):
								for q in range(0,10):
									for r in range(0,10):
										numlist=[i,j,k,l,m,n,o,p,q,r]
										if len(numlist)==len(set(numlist)):
											count+=1
										if count==1000000:
											print str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)
											exit(0)
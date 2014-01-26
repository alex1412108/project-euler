num=1
pnum=0
pnumbuf=0
numsum=0
while num+pnum<4000000:
	pnumbuf=num
	num+=pnum
	pnum=pnumbuf
	if num%2==0:
		numsum+=num
print numsum
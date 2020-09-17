limit=int(input(">>> "))
iter=3
prime=[]
while(iter<limit):
	for iter2 in range(2,iter):
		if(iter%iter2==0):
			prime.append(iter)
	iter=iter+1
for iter in range(2,limit):
	if(iter not in prime):
		print(iter,end=' ')		

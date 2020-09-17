k=int(input(">>> "))
i=3
l=[]
while(i<k):
	for j in range(2,i):
		if(i%j==0):
			l.append(i)
	i=i+1
for i in range(2,k):
	if(i not in l):
		print(i,end=' ')		
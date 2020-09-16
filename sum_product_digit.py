a=input("The number: ")
c=[]
e=[]
for b in a:
  c.append(int(b))
d=0
while(d<len(c)):
  e.append(int(c[d])*int(c[d+1]))
  d=d+2
print("\n\tProduct of digits:",sum(e))
print("\n\tSum of digits:",sum(c))
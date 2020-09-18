a=input()
b=int(input())
i=1
m=b/2
m=round(m)
j=round(b/2)
while(i<=b and m<=b):
  print(" "*m,a*i)
  if(i==b-1 or i==b):
    print(" "*j,"|")
    print(" "*j,"|")
  i=i+2
  m=m-1
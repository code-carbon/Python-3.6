num = int(input("Enter a number: "))
num1=num+1
for i in range (1, num1):
  if num%i==0:
    m=[i]
    print(m)
    if(num==i):
      o=len(m)
      print("There are ",o," factor(s) of",num)
 

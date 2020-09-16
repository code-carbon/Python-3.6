m=[0,1,]
i=int(input("Enter the number: "))
mw=True
while(mw==True):
  m.insert(len(m),m[-1]+m[-2])
  if(m[-1]==i):
    print(m[0:len(m)])
    mw=False
  elif(m[-1]>i):
    print(m[0:-1])  
    mw=False
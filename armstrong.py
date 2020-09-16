ar=input("~)")
m=[]
for a in ar:
  l=int(a)
  d=l**len(ar)
  m.append(d)
if(sum(m)==int(ar)):
  print("~} Truly Armstrong")
  input()
else:
  print("[E] Not Armstrong")
  input()

typeof = input()
value = []
if(typeof=="ord()"):
  string = input("Enter character: ")
  print()
  for a in string:
    value.append(ord(a))
    print("[",ord(a),"]",end=" ")
  print()
  print("\n[{(",sum(value),")}]")

elif(typeof=="chr()"):
  integer=input("Enter integer: ").split()
  print()
  for a in integer:
    a = int(a)
    print(chr(a),end="")
condition=True
code=[]
while condition == True:
  i=input(">>-> ")
  code.append(i)
  if(i=="run"):
    condition=False
print()
def print(i):
  return code[code.index("print:")+1].replace("[","").replace("]","").replace("'","")
def ask(i):
  return code[code.index("ask:")+1].replace("[","").replace("]","").replace("'","")
print_code="print:"
ask_code="ask:"
if print_code in code:
  print(print(i))
if ask_code in code:
  input(ask(i))



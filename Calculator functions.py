import os
def div(parser):
    value=parser[0]/parser[1]
    calc.pop(int(calc.index("/")-1))
    calc.pop(int(calc.index("/")+1))
    calc[calc.index("/")]=value
def pro(parser):
    value=parser[0]*parser[1]
    calc.pop(int(calc.index("*")-1))
    calc.pop(int(calc.index("*")+1))
    calc[calc.index("*")]=value
def add(parser):
    value=parser[0]+parser[1]
    calc.pop(int(calc.index("+")-1))
    calc.pop(int(calc.index("+")+1))
    calc[calc.index("+")]=value
def sub(parser):
    value=parser[0]-parser[1]
    calc.pop(int(calc.index("-")-1))
    calc.pop(int(calc.index("-")+1))
    calc[calc.index("-")]=value
if __name__=="__main__": 
    calc=input(">>> ").split()
    clear=lambda:os.system('cls')
    clear()
    if "/" in calc:
        parser=[int(calc[calc.index("/")-1]),int(calc[calc.index("/")+1])]
        div(parser)
    if "*" in calc:
        parser=[int(calc[calc.index("*")-1]),int(calc[calc.index("*")+1])]
        pro(parser)
    if "+" in calc:
        parser=[int(calc[calc.index("+")-1]),int(calc[calc.index("+")+1])]
        add(parser)
    if "-" in calc:
        parser=[int(calc[calc.index("-")-1]),int(calc[calc.index("-")+1])]
        sub(parser)
    if(len(calc)==1):
        print(">>>",calc[0])
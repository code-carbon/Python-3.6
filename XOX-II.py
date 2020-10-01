
import time
import os
cls=lambda:os.system("clear")
for i in range(0,101):
    print(">>> Loading application...",str(i)+"% <<<")
    time.sleep(0.001)
    cls()
x=["1","2","3","4","5","6","7","8","9"]
list=["O"]
bool=True
check=[]
mark='W'
X=[]
O=[]
def finish():
    breakpoint
    print("\n")
    print(x[:3])
    print(x[3:6])
    print(x[6:])
    breakpoint
    bool=False
def console():
    if mark in check:
        finish()
    else:
        print("\n")
        print(x[:3])
        print(x[3:6])
        print(x[6:])
        if(list[-1]=="X"):
            current="O"
        else:
            current="X"
        place=int(input(current+" >>> "))
        if(x[place-1]!="X" and x[place-1]!="O"):
            x[place-1]=current
        else:
            list.append(current)
            cheat(current)
        if(list[-1]=="X"):
            list.append("O")
        else:
            list.append("X")
        draw(x)

def draw(x):
    x_count=x.count("X")
    o_count=x.count("O")
    if(x_count+o_count==9):
        print("DRAW")
        finish()
    if(len(X)==3):
        print("Player O: WINNER [PLAYER X: 3 illegal moves]")
        finish()
    if(len(O)==3):
        print("Player X: WINNER [PLAYER O: 3 illegal moves]")
        finish()
    else:
        winner()
def winner():
    for i in range(0,9,3):
        if(x[i]==x[i+1]==x[i+2]):
            print(x[i],"is the winner...")
            check.append("W")
            finish() 
    for i in range(0,3): 
        if(x[i]==x[i+3]==x[i+6]):
            print(x[i],"is the winner...")
            check.append("W")
            finish() 
    if(x[0]==x[4]==x[8]):
        print(x[0],"is the winner...")
        check.append("W")
        finish()   
    if(x[2]==x[4]==x[6]):
        print(x[2],"is the winner...")
        check.append("W")
        finish()     
    console() 
def cheat(current):
    if(current=="X"):
        print("Player X: INVALID MOVE")
        X.append(1)
    else:
        print("Player O: INVALID MOVE")
        O.append(1)
if __name__ == '__main__':
    if(bool==True):
        console()

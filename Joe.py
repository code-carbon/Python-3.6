import os
def processor():
    for bunch in array:
        for cmd in bunch:
            if(cmd=="inp\""):
                inp()
def inp():
    string=""
    for a in array:
        string=string+str(a[a.index("inp\"")+1:a.index("\"\"")])
    input(string)
continuation=True
array=[]
while(continuation==True):
    code=input(">>> ")
    if(code=="RuN"):
        continuation=False
    else:
        array.append(code.split())
clear = lambda: os.system('cls')
clear()
processor()
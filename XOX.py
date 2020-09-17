j=["0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 "]
run=False
if(run==False):
    print(j[0:3])
    print(j[3:6])
    print(j[6:10])
    a=int(input("X: "))
    j=[" "," "," "," "," "," "," "," "," "]
    j[a]="X"
    print(j[0:3])
    print(j[3:6])
    print(j[6:10])
    print()
    b=int(input("O: "))
    if(b!=a):
        j[b]="O"
        print(j[0:3])
        print(j[3:6])
        print(j[6:10])
        print()
        c=int(input("X: "))
        if(c!=a and c!=b):
            j[c]="X"
            print(j[0:3])
            print(j[3:6])
            print(j[6:10])
            print()
          
            d=int(input("O: "))
            if(d!=a and d!=b and d!=c):
                j[d]="O"
                print(j[0:3])
                print(j[3:6])
                print(j[6:10])
                print()

                if(run==False):
                    e=int(input("X: "))
                    if(e!=a and e!=b and e!=c and e!=d):
                        j[e]="X"
                        if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[0],"WINS")
                                run=True
                        elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[0],"WINS")
                                run=True
                        elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[0],"WINS")
                                run=True
                        elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[1],"WINS")
                                run=True
                        elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[2],"WINS")
                                run=True
                        elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[2],"WINS")
                                run=True
                        elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[3],"WINS")
                                run=True
                        elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                print(j[0:3])
                                print(j[3:6])
                                print(j[6:10])
                                print(j[6],"WINS")
                                run=True
                        else:   
                            j[e]="X"
                            print(j[0:3])
                            print(j[3:6])
                            print(j[6:10])
                            print()
                            f=int(input("O: "))
                            if(f!=a and f!=b and f!=c and f!=d and f!=e):
                                if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[0],"WINS")
                                        run=True
                                elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[0],"WINS")
                                        run=True
                                elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[0],"WINS")
                                        run=True
                                elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[1],"WINS")
                                        run=True
                                elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[2],"WINS")
                                        run=True
                                elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[2],"WINS")
                                        run=True
                                elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[3],"WINS")
                                        run=True
                                elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print(j[6],"WINS")
                                        run=True
                                else:
                                        j[f]="O"
                                        print(j[0:3])
                                        print(j[3:6])
                                        print(j[6:10])
                                        print()
                                                        
                                        if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[0],"WINS")
                                                run=True
                                        elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[0],"WINS")
                                                run=True
                                        elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[0],"WINS")
                                                run=True
                                        elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[1],"WINS")
                                                run=True
                                        elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[2],"WINS")
                                                run=True
                                        elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[2],"WINS")
                                                run=True
                                        elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[3],"WINS")
                                                run=True
                                        elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print(j[6],"WINS")
                                                run=True
                                        else:
                                            g=int(input("X: "))
                                            if(g!=a and g!=b and g!=c and g!=d and g!=e and g!=f):
                                                j[g]="X"
                                                print(j[0:3])
                                                print(j[3:6])
                                                print(j[6:10])
                                                print()
                                                                        
                                                if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[0],"WINS")
                                                        run=True
                                                elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[0],"WINS")
                                                        run=True
                                                elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[0],"WINS")
                                                        run=True
                                                elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[1],"WINS")
                                                        run=True
                                                elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[2],"WINS")
                                                        run=True
                                                elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[2],"WINS")
                                                        run=True
                                                elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[3],"WINS")
                                                        run=True
                                                elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print(j[6],"WINS")
                                                        run=True
                                                else:
                                                    h=int(input("O: "))
                                                    j[h]="O"
                                                    if(h!=a and h!=b and h!=c and h!=d and h!=e and h!=f and h!=g):
                                                        print(j[0:3])
                                                        print(j[3:6])
                                                        print(j[6:10])
                                                        print()
                                                                                        
                                                        if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[0],"WINS")
                                                                run=True
                                                        elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[0],"WINS")
                                                                run=True
                                                        elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[0],"WINS")
                                                                run=True
                                                        elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[1],"WINS")
                                                                run=True
                                                        elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[2],"WINS")
                                                                run=True
                                                        elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[2],"WINS")
                                                                run=True
                                                        elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[3],"WINS")
                                                                run=True
                                                        elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                                                print(j[0:3])
                                                                print(j[3:6])
                                                                print(j[6:10])
                                                                print(j[6],"WINS")
                                                                run=True          
                                                        else:
                                                                i=int(input("X: "))
                                                                j[i]="X"
                                                                if(i!=a and i!=b and i!=c and i!=d and i!=e and i!=f and i!=g and i!=h):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print()
                                                                
                                                                                                        
                                                                if(j[0]==j[1]==j[2]=="X" or j[0]==j[1]==j[2]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[0],"WINS")
                                                                        run=True
                                                                elif(j[0]==j[3]==j[6]=="x" or j[0]==j[3]==j[6]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[0],"WINS")
                                                                        run=True
                                                                elif( j[0]==j[4]==j[8]=="X" or j[0]==j[4]==j[8]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[0],"WINS")
                                                                        run=True
                                                                elif( j[1]==j[4]==j[7]=="X" or j[1]==j[4]==j[7]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[1],"WINS")
                                                                        run=True
                                                                elif(j[2]==j[5]==j[8]=="X" or j[2]==j[5]==j[8]=="O" ):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[2],"WINS")
                                                                        run=True
                                                                elif(j[2]==j[6]==j[4]=="X" or j[2]==j[6]==j[4]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[2],"WINS")
                                                                        run=True
                                                                elif(j[3]==j[4]==j[5]=="X" or j[3]==j[4]==j[5]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[3],"WINS")
                                                                        run=True
                                                                elif(j[6]==j[7]==j[8]=="X" or j[6]==j[7]==j[8]=="O"):
                                                                        print(j[0:3])
                                                                        print(j[3:6])
                                                                        print(j[6:10])
                                                                        print(j[6],"WINS")
                                                                        run=True

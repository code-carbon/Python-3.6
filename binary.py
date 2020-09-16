def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
def Hello(n):
    return bin(n)
# Driver code  
if __name__ == '__main__':  
    n=int(input())
    print(decimalToBinary(n)) 
    m=str(decimalToBinary(n))
    k=m.count("0")
    l=m.count("1")
    print("Original: "+Hello(n))
    print("No. of 0's:",k)
    print("No. of 1's:",l)

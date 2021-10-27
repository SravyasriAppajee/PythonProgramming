a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
def largestnumber():
    if(a>=b) and (a>=c):
        largest=a
    elif(b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    print("largest number is: ",largest)
largestnumber()
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
if(a>=b) and(a>=c):
    highest=a
elif (b>=a) and (b>=c) :
    highest=b
else:
    highest=c
print("the largest number is:",highest)
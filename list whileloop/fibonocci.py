n= int(input("enter a limit for fibonocci series:"))
a,b=0,1
while a<n:
    print (a, end="")
    a,b =b, a+b
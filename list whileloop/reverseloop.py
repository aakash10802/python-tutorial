num =int(input("enter a num to reverse"))
sum = 0
while num > 0:
    sum=sum*10+num%10
    num //=10
    print("reverse of num is",sum)
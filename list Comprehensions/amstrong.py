num=int(input ("Enter a number: "))
org = num
l=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum+=digit**l
    num=num//10
if (sum==org):
    print(org,"is an Armstrong number")
else:
    print(org,"Not an Armstrong number")

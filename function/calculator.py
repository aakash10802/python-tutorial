def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


print("select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")
print("5.Exit")
while True:
    choice =input("Enter a choice(1/2/3/4/5):")
    if choice =='5':
        print("Exiting calculator")
        break
    if choice in ('1/2/3/4'):
        num1 = float(input("Enter first number:"))
        num2 = float (input("Enter second number:"))
        if choice =='1':
            print(num1,'+', num2,'=',add(num1,num2))
        elif choice =='2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice=='3':
            print(num1,'*',num2,'=',mul(num1,num2))
        elif choice =='4':
            if num1>num2:
                print(num1,'/',num2,'=',div(num1,num2))
            else:
                print("invalid division")
    else:
        print("invalid choice, pls try again.")
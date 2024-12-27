num=int(input("enter a number: "))
# for i in range(2, num):
#     if (num%i==0):
#         break
# else:
#     print(num,"is a perfect prime number.")
if not [i for i in range(2, num) if num % i == 0]:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
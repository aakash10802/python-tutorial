# # for loop --syntax


# for i in range(1,11,3): 
#     print(i)
    
    
# # in list
# d="python"
# for i in d:
#     print(i,end='')

# k=[]
# odd=[]
# for i in range(1,21):
#     if (i%2==0): 
#         k.append(i)
       
#     else:
#         odd.append(i)
        
# print(k)
# print(odd)
    


# d=[10,20,30,"hai","hello"]
# for i in d:
#     print(i)

# d=[10,20,21,22,26,28,29,2,33]
# sum =0
# pro=1
# for i in d:
#     if (i%2==0):   
#         sum+=i
#     else:
#         pro%=i
        
# print(sum)
# print(pro)

# s=[]
# p=[]
# u=[]
# for a in range(1,21):
#   if (a%5==0 and a%3==0):
#         s.append(a)
#   if (a%5==0 and a%3!=0):
#         p.append(a)
#   if (a%5!=0 and a%3==0):
#         u.append(a)
        
# print(s)
# print(p)
# print(u)

# get the maximum number from a list using for loop
f=[10,20,130,40,50]
max_number=f[0]
for i in f:
    if (i> max_number):
        max_number = i
print(max_number)


f=[10,20,130,40,50]
min_number=f[0]
for i in f:
    if (i< min_number):
        min_number = i
print(min_number)


d=[10,20,30,40,50]
l=[]
for i in d:
    l.insert(0,i)
        
print(l)


d=[10,90,20,10,10,20,10]
        
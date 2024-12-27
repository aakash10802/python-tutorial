m=[20,30,5,1,2.200,2200,2520]
max_num=m[0]
min_num=m[0]
for i in m:
    if(i>max_num):
        max_num=i
    
    if (i<min_num):
        min_num=i
        

print("max_num:",max_num)
print("min_num:",min_num)
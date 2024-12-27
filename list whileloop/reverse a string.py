r=input ("enter a string")
rev=""
i=len(r)-1
while i>=0:
    rev+=r[i]
    i-=1
print("Reversed String is:",rev)
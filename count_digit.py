a=abs(int(input()))
c=1
while a//10>0:
    a//=10
    c+=1
print(f"这是一个{c}位数")

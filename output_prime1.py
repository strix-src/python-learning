def isprime(a):
    if a<2:return False
    for c in range(2,int(a**0.5)+1):
        if a%c==0:
            return False
    return True

a=int(input("请输入一个数:"))
count=0

for i in range(2,a+1):
    if isprime(i):
        print(i,end=" ")
        count+=1
        if count%10==0:
            print()
print()

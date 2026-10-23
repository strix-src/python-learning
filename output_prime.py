print("请输入一个数")
a=int(input())
count=0
for i in range(2,a+1):
    isprime=1
    for c in range(2,i):
        if i%c==0:
            isprime=0
            break
    if isprime==1:
        count+=1
        print(i,end=" ")
        if count%10==0:
            print()
print()

import random
target=random.randint(0,1000)
count=0
print(f"请输入0~1000以内的猜测")
while True:
    count+=1
    attemps=int(input())
    if attemps<target:
        print("你输入的数字小了")
    elif attemps>target:
        print("你输入的数字大了")
    else :
        break
print(f"恭喜你答对了!一共输入了{count}")

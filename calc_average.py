print("请输入数字")
nums=list(map(int,input().split()))
if len(nums) == 0:
    print("你输入了0次")
else :
    total=sum(nums)
    count=len(nums)
    average=total/count
print(f"平均数是{average},共输入了{count}次")

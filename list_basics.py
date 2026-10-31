num=[]
a=input("请输入一串数字或其他：")
for i in a:
    num.append(i)
print(f"最后一个字符是{num.pop()}")
print(f"其余的字符是{num}")

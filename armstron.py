def nar(a):
    h=[]
    for i in range(10**(a-1),10**a):
           w=[int(j) for j in str(i)]
           total=0
           for digit in w:
               total+=digit**a
           if total==i:
               h.append(i)
    return h

if __name__=="__main__":
    try:
        while True:
            a=int(input("请输入大于0的数字:"))
            if a>1:
                break
    except ValueError:
        print("只允许输入数字")
    print(f"{a}位的阿姆斯特朗数有：{nar(a)}")

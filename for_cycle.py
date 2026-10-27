def factorial(x):
        if x<0:
            print("请输入大于0的数")
            return None
        result=1
        for i in range(1,x+1):
            result*=i
        return result

if __name__=="__main__":
    while True:
        try:
            y=int(input("请输入正整数:"))
            if y<0:
                  print("需要大于0")
                  continue
            break
        except ValueError:
                  print("只能是数字")
    r=factorial(y)
    print(f"这个数字的阶乘是{r}一共{len(str(r))}位")

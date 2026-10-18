a,b=map(int,input().split())
c=a//100*60+a%100+b
print(f"之后的时间是{c//60}:{c%60}")


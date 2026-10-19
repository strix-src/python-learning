hour1,minute1=map(int,input().split(":"))
hour2,minute2=map(int,input().split(":"))
tm=abs(hour1*60+minute1-hour2*60-minute2)
print(f"中间相隔了{tm//60}小时{tm%60}分钟")

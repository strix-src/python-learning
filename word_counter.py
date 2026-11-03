text=input('请输入一段内容：')
dic={}
for word in text:
    dic[word]=dic.get(word,0)+1
result=sorted(dic.items(),key=lambda w:w[1],reverse=True)
print(result)

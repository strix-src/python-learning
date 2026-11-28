start=0
chunk_size=8
overlap=2
chunks=[]
step=chunk_size-overlap
if step<=0:
    raise ValueError('chunk_size必须大于overlap')
text=input("请输入:")
if not text:
    raise ValueError('输入不能为空')
while start<len(text):
        chunk=text[start:start+chunk_size]
        chunks.append(chunk)
        start+=step
print(chunks)

import json,os
data={
        '今天':'偷懒',
        '明天':'打鱼'
        }
fn='data.json'
with open(fn,'w',encoding='utf-8')as f:
    json.dump(data,f)
if os.path.exists(fn):
    with open(fn,'r',encoding='utf-8')as f:
        result=json.load(f)
        print(result)


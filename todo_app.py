import os
fn = 'todo.txt'
tasks=[]
if os.path.exists(fn):
    with open (fn,'r',encoding='utf-8') as f:
        tasks=[x.strip() for x in f]
while True:
    print('1代表查看\n2代表添加\n3代表退出\n')
    chock=input('请输入你的选项:')
    if chock == '1':
        print(tasks)
    elif chock == '2':
        x = input('输入要添加的内容:')
        if x:
            tasks.append(x)
            with open (fn,'a',encoding='utf-8') as f:
                f.write(x+'\n') 
                print('添加成功')
    elif chock == '3':
        break
    else:
        print('输入不规范')

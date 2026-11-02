contact={
        '张三':123,
        '梁九':444,
        '王五':456
        }
print(contact)
contact['张三']=778
contact['李四']=233
print(f'新的为{contact}')
name=input('请输入名字:')
phone=contact.get(name,'查无此人')
print(f'最后查询的结果是{phone}')
deleted_phone=contact.pop('梁九')
deleted_phone=contact.pop('梁七','你错了')
print(deleted_phone)
print(f'使用pop新的为{contact}')
del contact['王五']
print(f'使用del新的为{contact}')
for name1,phone1 in contact.items():
    print(f'名字：{name1},电话：{phone1}')
print(list(contact.items()))
print(contact.items())

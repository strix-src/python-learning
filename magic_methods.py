class Dog:
    total_pet=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.total_pet+=1
    def __str__(self):
        return f'这只狗狗的名字是{self.name}年龄是{self.age}'
    def __del__(self):
        print(f'{self.name}离开了人间...')

dog1=Dog('旺仔',12)
dog2=Dog('佳佳',3)
print(dog1)
print(dog2)
print(f'狗子的总数是{Dog.total_pet}')
del dog1


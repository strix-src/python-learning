class Enity:
    def __init__(self,hp):
        self.hp=hp
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,amount):
        if amount<0:
            raise ValueError('不能小于0')
        self._hp=amount
class Snake(Enity):
    def __init__(self,hp,length):
        super().__init__(hp)
        self.length=length

a=Snake(10,10)
print(a.hp)
a.hp=100
print(a.hp)

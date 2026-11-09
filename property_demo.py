class Snake:
    def __init__(self,hp):
        self.hp=hp
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,v):
        if v<0:
            raise ValueError('血量不能为负')
        self._hp=v
        return self._hp
s=Snake(10)
print(s.hp)
s.hp=100
print(s.hp)

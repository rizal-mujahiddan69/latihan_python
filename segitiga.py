import math
from overloading import overload

class segitiga:
    def __init__(self, alas, tinggi):
        self.__alasan = alas
        self.__tinggian = tinggi
        self.__miring = math.sqrt(self.alasan**2 + self.tinggian**2)

    def luas(self):
        return (alasan*tinggian*0.5)

    def keliling(self):
        return alasan + tinggian + miring

    def __str__():
        print("alas :",alasan,"tinggi :",tinggi)
    
@overload
class segitiga:
    def __init__(self,a,b,c):
        self.__aa = a
        self.__bb = b
        self.__cc = c

    def luas(self):
        self.ss = (aa + bb + cc) / 2
        luasin = math.sqrt(ss * (ss - aa) * (ss - bb) * (ss - cc))
        return luasin

    def keliling(self):
        return self.aa + self.bb + self.cc


bangun = segitiga(12,20)
print(bangun)

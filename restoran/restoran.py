from menu import Menu
from employee import Employee
from girgitton import Ofitsiant
from oshpaz import Oshpaz
from klient import Klient

class Restoran:
    def __init__(self, name:str, location:str, menu: Menu) -> None:
        self.name = name
        self.location = location
        # self.menu = menu
        self.ishchilar = []
    
    def add_ishchi(self, obj: Employee):
        self.ishchilar.append(obj)
    
    def ishchilar_list(self):
        for i in self.ishchilar:
            print(i)

m1 = Menu("UzbTaomlari")
r1 = Restoran("Rayhon", "Chilonzor", m1)
kl1 = Klient()
o1 = Oshpaz("Muhriddin", 500, "Oshpaz")
ofit1 = Ofitsiant('Bobur', 25000, "Ofitsiant",m1)
ofit2 = Ofitsiant('Karim', 35000, "Ofitsiant",m1, True)

r1.add_ishchi(o1)
r1.add_ishchi(ofit1)
r1.add_ishchi(ofit2)

# m1.show_all_taomlar()

o1 = Oshpaz("Muhriddin", 500, "Oshpaz")
o1.taom_add('Osh', 25000, m1)
o1.taom_add("Norin", 21000, m1)
o1.taom_add("Halim", 28000, m1)
o1.taom_add("Somsa", 8000, m1)
o1.taom_add("Dumg'aza", 30000, m1)
o1.taom_add("Jiz", 35000, m1)
# m1.show_all_taomlar()

kl1.ofitsiant_chaqir(ofit1)
kl1.schetni_ber(ofit1)


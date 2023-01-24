from employee import Employee
from menu import Menu

class Ofitsiant(Employee):
    def __init__(self, name, maosh, kasbi, menu:Menu,bandlik=False):
        super().__init__(name, maosh, kasbi)
        self.bandlik = bandlik
        self.schet = 0
        self.menu = menu

    def zakaz_olish(self):
        taom = input("Nima hohlaysiz: ")
        miqdor = int(input("Nechta: "))
        self.schet += (self.menu.taomlar[taom]*miqdor)

    def taomlarni_klientga_korsat(self):
        self.menu.show_all_taomlar()
        self.zakaz_olish()

    def schet_ber(self):
        print(self.schet)
        self.bandlik = False
        self.schet = 0
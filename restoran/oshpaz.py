from menu import Menu
from employee import Employee

class Oshpaz(Employee):
    def taom_add(self, taom:str, narx:int, obj: Menu)->None:
        obj.taomlar.update({taom:narx})
        # obj.taomlar[taom] = narx # Shu ko'rinishda ham yozsa bo'ladi
    
    def taom_del(self, taom:str, obj: Menu):
        obj.taomlar.pop(taom)
    
    def change_taom_narx(self, taom:str, new_narx:int, obj: Menu)->None:
        obj.taomlar[taom] = new_narx
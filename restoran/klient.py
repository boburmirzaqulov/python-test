from girgitton import Ofitsiant

class Klient:
    def ofitsiant_chaqir(self, obj: Ofitsiant):
        if obj.bandlik == False:
            obj.bandlik = True
            self.taom_buyurtma_berish(obj)
            
    def taom_buyurtma_berish(self, obj: Ofitsiant):
        obj.taomlarni_klientga_korsat()
    
    def schetni_ber(self, obj: Ofitsiant):
        obj.schet_ber()
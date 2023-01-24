class Menu:
    def __init__(self, nomi, taomlar_royxati=None):
        self.nomi = nomi
        if taomlar_royxati == None:
            self.taomlar = {}
        else:
            self.taomlar = taomlar_royxati
    
    def show_all_taomlar(self):
        for key, value in self.taomlar.items():
            print(f"{key} narxi {value}")
    
 

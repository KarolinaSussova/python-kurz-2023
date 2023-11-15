class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return f"potvrzuji zapůjčení vozidla"            
        else:
            return f"vozidlo není k dispozici"
        
    def get_info(self):
        return f"Vámi vybrané vozidlo je {self.typ_vozidla} s registrační značkou {self.registracni_znacka}"
    

auto1 = Auto("4A2 3020", "Peugot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

def pujceni(vypujcka):
    if vypujcka == "Škoda":
        print(auto2.get_info())
        print(auto2.pujc_auto())
    elif vypujcka == "Peugot":
        print(auto1.get_info())
        print(auto1.pujc_auto()) 
    else:
        print("Tuto značku bohužel nemáme")

vypujcka = input("jaké auto si přejete půjčit? ")
pujceni(vypujcka)
vypujcka = input("jaké auto si přejete půjčit? ")
pujceni(vypujcka)
        





    



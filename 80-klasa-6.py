class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena

class Oprogramowanie(Produkt):
    def __init__(self, jezyk, system, nazwa, cena):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin

    def __str__(self):
        return f"Nazwa: {self.nazwa} Cena {self.cena} Jezyk {self.jezyk} Termin {self.termin}"

kl = Szkolenia("Szkolenie Python", 100 , "Python", "Windows", "2021.11.14")
# print(kl.nazwa, kl.cena, kl.jezyk, kl.system, kl.termin)
print(kl)

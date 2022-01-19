class Pracownik:
    def __init__(self, imie, nazwisko, kontrakt, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
        self.pensja = pensja

    def __str__(self):
        return f"Imie: {self.imie} Nazwisko {self.nazwisko} Kontratkr: {self.kontrakt} Pensja: {self.pensja}"

class DzialKard:

    def __init__(self):
        self.listraPracownikow = []

    def dodajPracownika(self, imie, nazwisko, kontrakt = "staz", pensja = 1000):
        pracownik = Pracownik(imie, nazwisko, kontrakt, pensja)
        self.listraPracownikow.append(pracownik)
        print("Pracownik zostal pomyslnie dodany")

    def pokazPracownikow(self):
        for i in self.listraPracownikow:
            print(f"{i.imie} {i.nazwisko}, Kontrakt: {i.kontrakt}, Pensja: {i.pensja}")

    def usunPracownika(self, nazwisko): 
        self.nazwisko = nazwisko
        for i in self.listraPracownikow:
            if (i.nazwisko == nazwisko):
                self.listraPracownikow.remove(i)

    def zmienKontrakt(self, nazwisko, pensja):
        self.pensja = pensja
        self.nazwisko = nazwisko
        for i in self.listraPracownikow:
            if(i.nazwisko == nazwisko):
                i.kontrakt = "etat"
                i.pensja = pensja

class Firma(DzialKard):

    def __init__(self, nazwaFirmy):
        super().__init__()
        self.nazwaFirmy = nazwaFirmy
        self.menu()

    def menu(self):

        print(f"Witaj w firmie {self.nazwaFirmy}")
        while(True):

            menu = input("D-dodaj pracownika, P-pokaz pracownikow, U-usun pracownika, Z-zmien kontrakt pracownikowi, K-koniec: ").upper()

            if(menu == "D"):
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                kontrakt = input("Podaj kontrakt staz/etat: ")
                if(kontrakt == "etat"):
                    pensja = int(input("Podaj pensje: "))
                    self.dodajPracownika(imie, nazwisko, kontrakt, pensja)
                elif(kontrakt == "staz"):
                    self.dodajPracownika(imie, nazwisko)
                else:
                    print("Podano bledny kontrakt")
            elif (menu == "P"):
                self.pokazPracownikow()
            elif (menu == "U"):
                nazwisko = input("Podaj nazwisko: ")
                self.usunPracownika(nazwisko)
            elif (menu == "Z"):
                nazwisko = input("Podaj nazwisko: ")
                pensja = input("Nowa pensja: ")
                self.zmienKontrakt(nazwisko, pensja)
            elif (menu == "K"):
                break

firma = Firma("Denek Corporation!")
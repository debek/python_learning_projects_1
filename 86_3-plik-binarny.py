import pickle

class Kontakt:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefony = []
        self.emaile = []

class KontaktController:
    def __init__(self):
        self.kontakty = []

    def dodajKontakt(self, imie, nazwisko):
        kontakt = Kontakt(imie, nazwisko)
        self.kontakty.append(kontakt)

    def usunKontakt(self, nazwisko):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                self.kontakty.remove(i)

    def dodajTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.telefony.append(telefon)

    def usunTelefon(self, nazwisko, telefon):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.telefony.remove(telefon)

    def dodajEmail(self, nazwisko, email):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.emaile.append(email)

    def usunEmail(self, nazwisko, email):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                i.emaile.remove(email)

    def wyswietlKontakty(self, nazwisko):
        for i in self.kontakty:
            if (i.nazwisko == nazwisko):
                print(f"Imie: {i.imie}, Nazwisko: {i.nazwisko}")
                for j in i.telefony:
                    print(f"Telefon: {j}")
                for k in i.emaile:
                    print(f"Email: {k}")

class App(KontaktController):

    def __init__(self):
        super().__init__()
        try:
            plik = open("86_3.dat", "rb")
            self.kontakty = pickle.load(plik)
            plik.close()
        except:
            plik = open("86_3.dat", "wb")
            pickle.dump([], plik)
            plik.close()

        self.menu()

    def menu(self):

        while (True):

            menu = input("1-dodaj kontakt, 2-pokaz kontakty, 3-usun kontakt, "
                         "\n4-dodaj telefon, 5-usun telefon, 6-dodaj email, 7-usun email, 8-koniec: ")

            if (menu == "1"):
                imie = input("Podaj imie: ")
                nazwisko = input("Podaj nazwisko: ")
                self.dodajKontakt(imie, nazwisko)
            elif (menu == "2"):
                nazwisko = input("Podaj nazwisko: ")
                self.wyswietlKontakty(nazwisko)
            elif (menu == "3"):
                nazwisko = input("Podaj nazwisko: ")
                self.usunKontakt(nazwisko)
            elif (menu == "4"):
                nazwisko = input("Podaj nazwisko: ")
                telefon = input("Podaj telefon: ")
                self.dodajTelefon(nazwisko, telefon)
            elif (menu == "5"):
                nazwisko = input("Podaj nazwisko: ")
                telefon = input("Podaj telefon: ")
                self.usunTelefon(nazwisko, telefon)
            elif (menu == "6"):
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                self.dodajEmail(nazwisko, email)
            elif (menu == "7"):
                nazwisko = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                self.usunEmail(nazwisko, email)
            elif (menu == "8"):

                plik = open("86_3.dat", "wb")
                pickle.dump(self.kontakty, plik)
                plik.close()
                break
app = App()

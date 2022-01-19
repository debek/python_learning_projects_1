class Kontakt:
    def __init__(self, imie, nazwisko, email, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon

listaKontaktow = []

while(True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-Koniec: ").upper()
    if menu == "D":
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        email = input("Podaj email: ")
        telefon = input("Podaj telefon: ")

        kontakt = Kontakt(imie, nazwisko, email, telefon)
        listaKontaktow.append(kontakt)
        print("Pomyslnie dodano nowy kontakt")

    elif (menu == "P"):
        for i in listaKontaktow:
            print(f"Imie: {i.imie}, {i.nazwisko}, {i.email}, {i.telefon}")
    elif (menu == "U"):

        znaleziono = False
        usunac = input("Podaj nazwisko kogo usunac: ")
        for i in listaKontaktow:
            if i.nazwisko == usunac:
                znaleziono = True
                listaKontaktow.remove(i)
                print("Pomyslnie usunieto")
                break
            if znaleziono == False:
                print("Nie znaleziono")

    elif (menu == "Z"):
        znaleziono = False
        zmienic = input("Podaj nazwisko, które edytować: ")
        for i in listaKontaktow:
            if i.nazwisko == zmienic:
                znaleziono = True
                coedytowac = input("Co chcesz edytowac?: ")
                nazwa = input("Podaj nowa wartosc: ")
                if(coedytowac == "imie"):
                    i.imie = nazwa

            if znaleziono == False:
                print("Nie znaleziono")

    elif (menu == "K"):
        break
    else:
        print("Nierozpoznana opcja menu")

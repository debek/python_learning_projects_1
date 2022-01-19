class Student:
    def __init__(self):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []

    def dodajOcene(self, ocena):
        self.oceny.append(ocena)
        return ocena

    def wypiszOceny(self):
        for i in self.oceny:
            print(i)

    def policzSredna(self):
        liczba_ocen = len(self.oceny)
        suma = 0
        for i in self.oceny:
            suma += i

        srednia = suma/liczba_ocen
        return srednia

listastudentow = []

while(True):

    menu = input("D-dodaj studenta, P-pokaz studentów, U-usun studenta, O-dodaj ocene studentowi, "
                 "W-wypisz oceny studenta, S-srednia studenta, K-koniec: ").upper()

    if(menu == "D"):
        imie = input("Podaj imie studenta: ")
        nazwisko = input("Podaj nazwisko studenta: ")
        st1 = Student()
        st1.imie = imie
        st1.nazwisko = nazwisko
        listastudentow.append(st1)
    elif(menu == "P"):
        for i in listastudentow:
            print(f"{i.imie} {i.nazwisko}")
    elif (menu == "U"):
        znaleziono = False
        nazwa = input("Podaj nazwisko kogo usunac: ")
        for i in listastudentow:
            if i.nazwisko == nazwa:
                znaleziono = True
                listastudentow.remove(i)
                print("Pomyslnie usunieto")
                break
            elif znaleziono == False:
                print("Nie znaleziono")
    elif (menu == "O"):
        znaleziono = False
        nazwa = input("Podaj nazwisko studenta: ")
        ocena = int(input("Podaj ocene: "))
        for i in listastudentow:
            if i.nazwisko == nazwa:
                znaleziono = True
                i.dodajOcene(ocena)
                print("Pomyslnie dodano")
                break
            elif znaleziono == False:
                print("Nie znaleziono")
    elif (menu == "W"):
        znaleziono = False
        nazwa = input("Podaj nazwisko studenta: ")
        for i in listastudentow:
            if nazwa == i.nazwisko:
                i.wypiszOceny()
                break
            elif znaleziono == False:
                print("Nie znaleziono")

    elif (menu == "S"):
        znaleziono = False
        nazwa = input("Podaj nazwisko studenta: ")
        for i in listastudentow:
            if nazwa == i.nazwisko:
                print(f"Srednia ocen tego studenta to {i.policzSredna()}")
            elif znaleziono == False:
                print("Nie znaleziono")
    elif (menu == "K"):
        break
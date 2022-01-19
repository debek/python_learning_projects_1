class Kurs:
     def __init__(self, nazwa, termin, miasto):
          self.nazwa = nazwa
          self.termin = termin
          self.miasto = miasto
          self.uczestnicy = []

class Kursant:
     def __init__(self, imie, nazwisko, telefon):
          self.imie = imie
          self.nazwisko = nazwisko
          self.telefon = telefon

listaKursow = []
while(True):

    print("System dla firmy szkoleniowej")
    menu = int(input("1-Dodaj kurs, 2-Wyświetl kursy, 3-Usuń kurs, 4-Dodaj kursanta do kursu, 5-Wyświetl kurs wraz z kursantami, "
                 "6-Usuń kursanta z kursu, 7-koniec: "))

    if(menu == 1):
        nazwa = input("Podaj nazwę kursu: ")
        termin = input("Podaj termin kursu: ")
        miasto = input("Podaj miasto kursu: ")
        kurs = Kurs(nazwa, termin, miasto)
        listaKursow.append(kurs)

    elif(menu == 2):
        for i in listaKursow:
             print(f"{i.nazwa}, {i.termin}, {i.miasto}")
    elif (menu == 3):
        nazwa = input("Podaj nazwę kursu: ")
        for i in listaKursow:
             if i.nazwa == nazwa:
                  listaKursow.remove(i)
    elif (menu == 4):
        nazwaKursu = input("Podaj nazwe kursu: ")
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj telefon: ")

        kursant = Kursant(imie, nazwisko, telefon)

        for i in listaKursow:
             if i.nazwa == nazwaKursu:
                  i.uczestnicy.append(kursant)

    elif (menu == 5):
        nazwaKursu = input("Podaj nazwe kursu: ")
        for i in listaKursow:
             if i.nazwa == nazwaKursu:
                 for i in i.uczestnicy:
                     print(f"{i.imie}, {i.nazwisko}, {i.telefon}")

    elif (menu == 6):
        nazwaKursu = input("Podaj nazwę kursu: ")
        nazwisko = input("Podaj nazwisko: ")

        for i in listaKursow:

            if i.nazwa == nazwaKursu:
                for j in i.uczestnicy:
                    if j.nazwisko == nazwisko:
                        print(j.nazwisko)
                        i.uczestnicy.remove(j)

    elif (menu == 7):
        print("koniec")
        break
    else:
        print("Nierozpoznana opcja menu")

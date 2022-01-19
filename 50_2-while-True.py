kontakty = []

while(True):

    menu = input("D-dodaj, P-pokaz, U-usun, Z-zmien, K-koniec: ").upper()

    if(menu == "D"):
        # pytania: imie, nazwisko, telefon
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj numer telefonu: ")

        kontakt = [imie, nazwisko, telefon]
        kontakty.append(kontakt)
        print("Pomyślnie dodano kontakt")
    elif (menu == "P"):
        for kontakt in kontakty:
            print(f"Imie: {kontakt[0]}, Nazwisko: {kontakt[1]}, Telefon: {kontakt[2]}")
    elif (menu == "U"):
        nazwisko = input("Podaj nazwisko kontaktu do usunięcia: ")
# # MOJE ROZWIAZANIE - nie do konca okej. W domu przeanalizowac na spokojnie
#         for i in kontakty:
#             if (nazwisko in i): ## problem z nazwiskiem moze byc: Now, Nowak, Nowacki. In znajdzie Now w pierwszym wystapieniu. Lepiej szukac po indexie a nie po stringu. Moge natrafic np. na imie
#                 i.remove()
#                 print("Pomyślnie usunieto kontakt")
#                 break
# Roberta ROZWIAZANIE
        znaleziono = False
        for i in kontakty:
            if (i[1] == nazwisko):
                znaleziono = True
                kontakty.remove(i)
                print("Pomyślnie usunieto kontakt")
                break
        if(znaleziono == False):
            print("Nie znaleziono kontaktu")

    elif (menu == "Z"):
        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon
        nazwisko = input("Podaj nazwisko kontaktu do zmiany: ")
        noweImie = input("Podaj nowe imie kontaktu do zmiany: ")
        noweNazwisko = input("Podaj nowe nazwisko kontaktu do zmiany: ")
        nowyTelefon = input("Podaj nowy telefon kontaktu do zmiany: ")

# # Moje rozwiazanie nie dziala. Zrozumiec dlaczego
#         for i in kontakty:
#             index = -1
#             index = index + 1
#             if (i[1] == nazwisko):
#                 kontakty[index][0] = noweImie
#                 kontakty[index][1] = noweNazwisko
#                 kontakty[index][2] = nowyTelefon
#                 break
# Rozwiazanie Roberta
        znaleziono = False
        for i in kontakty:
            if (i[1] == nazwisko):
                znaleziono = True
                i[0] = noweImie
                i[1] = noweNazwisko
                i[2] = nowyTelefon
                print("Pomyślnie zaktualizowano")
                break

        if(znaleziono == False):
            print("Nie znaleziono kontaktu")

    elif (menu == "K"):
        print("koniec programu")
        break
    else:
        print("nierozpoznana opcja menu")
        break
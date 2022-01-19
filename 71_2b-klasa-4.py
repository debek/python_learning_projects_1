sklep = {"chleb":2.50, "sok":3.50, "woda":1.25}
koszyk = []

while(True):

    menu = input("D-dodaj pordukt, P-podglad koszyka, K-kasa/koniec: ").upper()

    if(menu == "D"):
        print("Oferta sklepu")
        for produkt in sklep:
            print(f"Produkt: {produkt} Cena: {sklep[produkt]}")

        towar = input("Podaj nazwę produktu, ktory chcesz kupić: ")
        if(towar in sklep):
            koszyk.append(towar)
        else:
            print(f"Brak produktu w sklepie")

    elif(menu == "P"):
        print("Zawartość Twojego koszyka: ")
        for index, produkt in enumerate(koszyk):
            print(f"Produkt ({index+1}): {produkt}")

    elif(menu == "K"):
        print("Podsumowanie")
        suma = 0


        print(f"Razem do zaplaty jest: {suma}")
        break

    else:
        print("Nierozpoznana opcja menu")

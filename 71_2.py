class Koszyk:
                                                                                                                                    
    def __init__(self):
        self.zakupy = {}

    def dodajProdukt(self, produkt, ilosc):

        if produkt in self.zakupy:
            self.zakupy[produkt] += ilosc
        else:
            self.zakupy[produkt] = ilosc

    def usunProdukt(self, produkt, ilosc):

        if self.zakupy[produkt] > ilosc:
            self.zakupy[produkt] -= ilosc

        elif self.zakupy[produkt] == ilosc:
            self.zakupy.pop(produkt)

        elif self.zakupy[produkt] < ilosc:
            print("Za dużo chcesz usunąć!")

sklep = {"chleb":2.50, "sok":1.80, "woda":2.80, "piwo":5.55}
koszyk = Koszyk()

while(True):

    menu = input("Witaj w sklepie !!!\nD-dodaj produkt, P-pokaz zawartosc koszyka, U-usun produkt, K-kasa/koniec: ").upper()

    if(menu == "D"):
        produkt = input("Podaj produkt: ")
        if produkt in sklep:
            ilosc = int(input("Podaj ilosc: "))
            koszyk.dodajProdukt(produkt, ilosc)

    elif (menu == "P"):
        for i in koszyk.zakupy:
            print(f"Produkt: {i}, ilosc {koszyk.zakupy[i]}")

    elif (menu == "U"):
        produkt = input("Podaj produkt: ")
        for i in koszyk.zakupy:
            if produkt == i:
                ilosc = int(input("Podaj ilosc: "))
                koszyk.usunProdukt(produkt, ilosc)

    elif (menu == "K"):
        print("PARAGON")
        cena_koncowa = 0
        for i in koszyk.zakupy:
            cena = sklep[i]
            wartosc = koszyk.zakupy[i] * cena
            cena_koncowa += wartosc
            print(f"Produkt: {i}, Ilość: {koszyk.zakupy[i]}, Cena:{cena}, Wartość: {wartosc}")
        print(f"RAZEM DO ZAPLATY:: {cena_koncowa}")
        break

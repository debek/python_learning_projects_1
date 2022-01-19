class Przychodnia:
    def __init__(self, nazwa, miasto):
        self.nazwa = nazwa
        self.miasto = miasto
        self.pacjenci = []

class Pacjent:
    def __init__(self):
        self.choroby = []

class Controler(Przychodnia):
    def __init__(self):
        self.przychodnie = []
        pass

    def dodajPrzychodnie(self, nazwa, miasto):
        przychodnia = Przychodnia(nazwa, miasto)
        self.przychodnie.append(przychodnia)
        print("Przychodnia zostala pomyslnie dodana")

    def usunPrzychodnie(self, nazwa):
        self.przychodnie.remove(nazwa)
        print("Przychodnia zostala pomyslnie usunieta")

    def dodajPacjenta(self):
        pass
    def usunPacjenta(self):
        pass
    def listaPrzychodnie(self):
        pass
    def listaPacjentow(self):
        pass
    def dodajChorobe(self):
        pass
    def listaChorob(self):
        pass

class Menu(Controler):
    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        print(f"System NFZ")

        while True:
            print(f"1 - Przychodnia, 2 - Pacjent, 3 - Koniec")
            menu = input("Podaj numer: ")

            if (menu == "1"):
                menu1 = input(
                    f"1 - dodaj przychodnie, 2 - usun przychodnie, 3 - dodaj pacjenta do przychodni, 4 - lista przychodni, 5 - lista pacjentow w przychodni: ")
                if (menu1 == "1"):
                    nazwa = input("Podaj nazawe: ")
                    miasto = input("Podaj miasto: ")
                    # super().dodajPrzychodnie(nazwa, miasto)
                    self.dodajPrzychodnie(nazwa, miasto)

                elif (menu1 == "2"):
                    pass
                elif (menu1 == "3"):
                    pass
                elif (menu1 == "4"):
                    print(self.przychodnie)
                    for i in self.przychodnie:
                        print(f"{i.nazwa}")
                elif (menu1 == "5"):
                    pass
                else:
                    print(f"Podaj wartosci od 1-5")

            elif (menu == "2"):
                menu2 = input(f"1 - dodaj chorobe pacjentowi, 2 - lista chorob pacjenta: ")
                if (menu2 == "1"):
                    pass
                elif (menu2 == "2"):
                    pass
                else:
                    print(f"Podaj wartosci od 1-2")
                    pass

            elif (menu == "3"):
                break
            else:
                print("Podany numer jest zly. Podaj numer od 1-3")

przychodnia = Menu()

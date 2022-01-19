import random

losowa_liczba = random.randint(1, 100)
# losowa_liczba = 2
proby = 0

print("Za duzo za malo. Komputer losuje liczbe z przedzialu 1-100. Zgadniej jaką liczbe wylosował")

while True:
    liczba_zgadywana = int(input("Podaj liczbe: "))
    if (liczba_zgadywana == losowa_liczba):
        print("Gratulacje")
        pytanie = input("Czy grasz jeszcze raz? T-Tak, N-Nie: ").upper()
        if (pytanie == "T"):
            proby = 0
            continue
        else:
            break
    elif(proby != 4):
        proby = proby + 1
        if (losowa_liczba > liczba_zgadywana):
            print("Wieksza od wylosowanej")
        elif (losowa_liczba < liczba_zgadywana):
            print("Mniejsza od wylosowanej")
        continue
    elif proby == 4:
        pytanie = input("Czy grasz jeszcze raz? T-Tak, N-Nie: ").upper()
        if(pytanie == "T"):
            proby = 0
            continue
        else:
            print("Koniec gry")
            break

kina = ["Cinema-City", "Multikino"]
filmy = {0 : ["Matrix", "Avatar", "Shrek"], 1 : ["Piraci z Karaibów", "Król Lew", "Władca Pierścieni"]}
litery = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
cenaBilet = 18.00

# ID kina
id_kina = -1

while (True):
    try:
        id_kina = int(input("Podaj ID kina: "))
        print(f"Podano kino: {kina[id_kina]}")
    except ValueError:
        print("Podaj wartość od 0 do 1")
    except IndexError:
        print("Poza zakresm")
    else:
        break

index_filmu = -1
while(True):
    try:
        index_filmu = int(input("Podaj index filmu: "))
        print(f"Podano film: {filmy[id_kina][index_filmu]}")
    except ValueError:
        print("Podaj wartość od 0 do 3")
    except IndexError:
        print("Poza zakresm")
    else:
        break

ilosc_osob = -1
while(True):
    try:
        ilosc_osob = int(input("Podaj ilość osób: "))
        print(f"Ilość osób: {ilosc_osob}")
    except ValueError:
        print("Podaj liczbe")
    else:
        break

# Sprawdzenie imiona
flaga = False
imie = input("Podaj imie: ")
for i in imie:
    if (i in litery):
        flaga = True
    else:
        flaga = False
        break

if (flaga == True):
    print(f"Imię osoby rezerwującej {imie}")
else:
    print(f"Podaj male polskie litery dla imienia")


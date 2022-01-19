import random

def wyliczenie(dane):

    #najwieksza wartosc
    max = 0
    for i in dane:
        if i > max:
            max = i

    #najmniejsza wartosc
    min = 101
    for i in dane:
        if i < min:
            min = i

    #srednia wartosc
    srednia = 0
    for i in dane:
        srednia = srednia + i
    srednia = srednia / len(dane)

    #ilosc liczb parzystych
    parzyste = 0
    for i in dane:
        if i % 2 == 0:
            parzyste = parzyste +1

    #ilosc liczb nieparzystych
    nieparzyste = 0
    for i in dane:
        if i % 2 != 0:
            nieparzyste = nieparzyste +1

    return max, min, srednia, parzyste, nieparzyste

lista = []

for i in range(10):
    los = random.randint(1, 100)
    lista.append(los)

print(lista)
wynik = wyliczenie(lista)
print(wynik)

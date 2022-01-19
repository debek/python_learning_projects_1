import random

lista1 = []
lista2 = []

for i in range(10):
    los = random.randint(1,50)
    lista1.append(los)
    los = random.randint(1,50)
    lista2.append(los)

for i in lista1:
    for x in lista2:
        if (i == x):
            print(f"{i} wystepuje dwa razy")

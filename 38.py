liczba1 = int(input("Podaj liczbe a: "))
liczba2 = int(input("Podaj liczbe b: "))
liczba3 = int(input("Podaj liczbe c: "))

# # Sposob 1
# zbior = {liczba1, liczba2, liczba3}
# print(zbior.union())

# Sposob 2
if liczba1 < liczba2 and liczba1 < liczba3:
    print(liczba1)
    if liczba2 < liczba3:
        print(liczba2)
        print(liczba3)
    else:
        print(liczba3)
        print(liczba2)
elif liczba2 < liczba1 and liczba2 < liczba3:
    print(liczba2)
    if liczba1 < liczba2:
        print(liczba1)
        print(liczba3)
    else:
        print(liczba3)
        print(liczba1)
elif liczba3 < liczba1 and liczba3 < liczba2:
    print(liczba3)
    if liczba2 < liczba1:
        print(liczba2)
        print(liczba1)
    else:
        print(liczba1)
        print(liczba2)
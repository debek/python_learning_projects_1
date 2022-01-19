liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
liczba3 = int(input("Podaj liczbe 3: "))

if liczba1 > liczba2 and liczba1 > liczba3:
    print(f"Liczba 1 jest najwieksza")
elif liczba2 > liczba1 and liczba2 > liczba3:
    print(f"Liczba 2 jest najwieksza")
elif liczba3 > liczba1 and liczba3 > liczba2:
    print(f"Liczba 3 jest najwieksza")

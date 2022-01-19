podstawa = int(input("Podaj podstawe: "))
wykladnik = int(input("Podaj wykladnik: "))
suma = 1

for i in range(wykladnik):
    suma = suma * podstawa

if suma <= 0:
    print("Suma nie moze wynosic zero")
else:
    print(f"{suma}")

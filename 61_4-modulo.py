suma = 0

for i in range(5):
    liczba = int(input(f"Podaj liczbe {i}: "))
    if liczba % 2 == 0:
        suma = suma + liczba

print(suma)

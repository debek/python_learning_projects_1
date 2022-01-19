silnia = int(input("Podaj liczbe silni: "))
wynik = 1

for i in range(1, silnia +1):
    wynik = wynik * i

print(f"Silnia wynosi: {wynik}")

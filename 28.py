pytanie = input("Podaj ciag znakow: ")
znaki = len(pytanie)
spacje1 = pytanie.count(" ")
spacje2 = pytanie.replace(" ", "")
spacje2 = len(spacje2)
spacje2 = znaki - spacje2

print(f"Liczba znakow to: {znaki}" )
print(f"Liczba spacji to: {spacje1}" )
print(f"Liczba spacji to: {spacje2}" )

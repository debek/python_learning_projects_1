# Konkatynacja
zm1 = "poznajemy"
zm2 = "Pythona"
zm3 = "Dzisiaj"
zm4 = "wiele"

print(zm3 + " " + zm1 + " mozliwosci " + zm2 + ", " + "których jest " + zm4 + ".")

# Uproszczona wersja od wersji 3.6. Fstring

imie = "Daniel"
wiek = "XX"
print(f"Mam na imie {imie} i mam {wiek} lat")

###
zm1 = "ciekawe"
zm2 = "programowanie"
zm3 = "jest"
zm4 = "wciagajace"
zm5 = "i"
pomoc = ""

pomoc = zm1
zm1 = zm2
zm2 = zm3
zm3 = pomoc
pomoc = zm4
zm4 = zm5
zm5 = pomoc

print(zm1, zm2, zm3, zm4, zm5)
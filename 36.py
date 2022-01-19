slownik = {
    "zero":0,
    "jeden":1,
    "dwa":2,
    "trzy":3,
    "cztery":4,
    "piec":5,
    "szesc":6,
    "siedem":7,
    "osiem":8,
    "dziewiec":9
}

l1 = input("Podaj liczbe pierwsza: ")
l2 = input("Podaj liczbe druga: ")

suma = slownik[l1] + slownik[l2]

print(f"Suma: {suma}")

import matplotlib.pyplot as plt

plik = open("studenci.txt", "r", encoding="utf8")

dane = plik.readlines()
warszawa = 0
szczecin = 0
bydgoszcz = 0

for i in dane:
    x = i.split(";")
    if (x[2].strip() == "Warszawa"):
        warszawa += 1
    elif (x[2].strip() == "Szczecin"):
        szczecin += 1
    elif (x[2].strip() == "Bydgoszcz"):
        bydgoszcz += 1
    else:
        pass

dane = []
dane.append(warszawa)
dane.append(szczecin)
dane.append(bydgoszcz)

info = ["Warszawa", "Szczecin", "Bydgoszcz"]

plt.bar(info, dane)
plt.title('Prezentacja danych')
plt.show()

plik.close()
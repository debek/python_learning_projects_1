# dane1 = [1,3,5]
# dane2 = [4,1,2]
#
# suma = dane1[0]+dane1[1]+dane1[2]+dane2[0]+dane2[1]+dane2[2]
#
# print(f"{suma}")

##################
lista = []

l1 = int(input("Podaj liczbe: "))
l2 = int(input("Podaj liczbe: "))
l3 = int(input("Podaj liczbe: "))
l4 = int(input("Podaj liczbe: "))
l5 = int(input("Podaj liczbe: "))

lista.append(l1)
lista.append(l2)
lista.append(l3)
lista.append(l4)
lista.append(l5)

print(f"{lista}")

suma = l1 + l2 + l3 + l4 + l5
srednia = suma / len(lista)

print(f"Suma to: {suma}")
print(f"Srednia to: {srednia}")
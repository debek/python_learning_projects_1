dane = [3, 43, 56, 75, 87, 45, 65, 84]
print(f"{dane[0]}")

#Sposob1
print(f"{dane[-1]}")

#Sposob2
dane.reverse()
print(f"{dane[0]}")

#Sposob3
dane2 = dane.pop(0)
print(f"{dane2}")

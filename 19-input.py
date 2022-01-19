import random

los1 = int(random.randint(1,10))
los2 = int(random.randint(1,10))
wynik = los1 * los2

wynik_uzytkownika=int(input(f"Ile to jest {los1} * {los2}: "))

print(f"Odpowiedz uzytkownika {wynik_uzytkownika}")
print(f"Odpowiedz komputera {wynik}")

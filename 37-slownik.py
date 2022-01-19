slownik = {
    "1":"jeden",
    "2":"dwa",
    "3":"trzy",
    "4":"cztery",
    "5":"piec",
    "6":"szesc",
    "7":"siedem",
    "8":"osiem",
    "9":"dziewiec",
    "0":"zero"
}

liczba = input("Podaj czterocyfrowa liczbe: ")

znak1 = liczba[0]
znak2 = liczba[1]
znak3 = liczba[2]
znak4 = liczba[3]

print(slownik[znak1], slownik[znak2], slownik[znak3], slownik[znak4])

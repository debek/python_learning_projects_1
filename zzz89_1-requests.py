import requests

res = requests.get("https://api.chucknorris.io/jokes/categories")
tytul = res.json()

pytanie = input("Podaj kateogrie, która Cię interesuje: ")
for i in tytul:
    if (i == pytanie):
        zart = requests.get(f"https://api.chucknorris.io/jokes/random?category={pytanie}")
        zart_get = zart.json()
        zart = zart_get["value"]
        zart_final = zart.replace ("Chuck Norris", "Daniel Debny")
        print(zart_final)

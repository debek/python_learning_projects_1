import pymysql

try:
    conn = pymysql.connect(host="127.0.0.1", user="root", password="alxalx", database="db93", charset="utf8")
    c = conn.cursor()
    print("Polaczenie OK")
except:
    print("Blad polaczenia z baza danych")

def dodaj(imie, nazwisko, pensja):
    sql = f"INSERT INTO pracownicy(imie, nazwisko, pensja) VALUES ('{imie}', '{nazwisko}', '{pensja}');"
    c.execute(sql)

    dec = input("Czy na pewno dodac dane do bazy danych? T/N: ").upper()
    if (dec == "T"):
        conn.commit()
        print("Dane zostaly dodane pomyslnie")
    else:
        conn.rollback()
        print("Operacja zostala anulowana")

def pokaz():
    c.execute("SELECT * FROM pracownicy")
    dane = c.fetchall()
    for row in dane:
        print(f"{row[0]}:, {row[1]}:, {row[2]}:, {row[3]} PLN")

def usun(nazwisko):
    c.execute(f"SELECT * FROM pracownicy WHERE nazwisko = '{nazwisko}'")
    dane = c.fetchall()

    if (len(dane) > 0):
        sql = f"DELETE FROM pracownicy WHERE nazwisko = '{nazwisko}'"
        c.execute(sql)
        dec = input("Czy na pewno usunac dane z bazy danych? T/N: ").upper()
        if (dec == "T"):
            conn.commit()
            print("Dane zostaly usuniete pomyslnie")
        else:
            conn.rollback()
            print("Operacja zostala anulowana")
    else:
        print("Nie znaleziono danych")

def zmien(nazwisko, noweImie, noweNazwisko, nowaPensja):
    c.execute(f"SELECT * FROM pracownicy WHERE nazwisko = '{nazwisko}'")
    dane = c.fetchall()

    if (len(dane) > 0):
        sql = f"UPDATE pracownicy SET imie = '{noweImie}', nazwisko='{noweNazwisko}', pensja='{nowaPensja}' WHERE nazwisko='{nazwisko}'"
        c.execute(sql)
        dec = input("Czy na pewno usunac dane z bazy danych? T/N: ").upper()
        if (dec == "T"):
            conn.commit()
            print("Dane zostaly usuniete pomyslnie")
        else:
            conn.rollback()
            print("Operacja zostala anulowana")
    else:
        print("Nie znaleziono danych")

def wyszukiwanie(szukanie):
    c.execute(f"SELECT * FROM pracownicy WHERE nazwisko like '%{szukanie}%' OR imie like '%{szukanie}%'")
    dane = c.fetchall()
    for i in dane:
        print(i[0], i[1], i[2], i[3])

while(True):

    menu = input("1-dodaj pracownika, 2-wyswietl pracownikow, 3-usun parcownika, 4-zmien dane pracownikowi, 5-wyszukiwanie, 6-koniec: ")

    if(menu == "1"):
        imie = input("Podaj imie: ")
        nazwisko = input("Podaj nazwisko: ")
        pensja = int(input("Podaj pensje: "))
        dodaj(imie, nazwisko, pensja)

    elif (menu == "2"):
        pokaz()

    elif (menu == "3"):
        nazwisko = input("Podaj nazwisko: ")
        usun(nazwisko)

    elif (menu == "4"):
        nazwisko = input("Podaj nazwisko: ")
        noweImie = input("Podaj nowe imie: ")
        noweNazwisko = input("Podaj nowe nazwisko: ")
        nowaPensja = input("Podaj nowa pensje: ")
        zmien(nazwisko, noweImie, noweNazwisko, nowaPensja)

    elif (menu == "5"):
        szukanie = input("Kogo chcesz znalezc?: ")
        wyszukiwanie(szukanie)

    elif (menu == "6"):
        break

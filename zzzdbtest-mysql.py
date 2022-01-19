import pymysql

try:
    conn = pymysql.connect(host="127.0.0.1", user="root", password="alxalx", database="testowa", charset="utf8")
    c = conn.cursor()
    print("Polaczenie OK")
except:
    print("Blad polaczenia z baza danych")

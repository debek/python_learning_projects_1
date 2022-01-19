import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")
print(df)

# wyswietlenie danych kolumny
print(df['Kraj'])
print(df[["Kraj","Sprzedawca"]])

# wyswietl utarg powyzej 3000
print(df["utarg" > 3000])
print(df[("utarg" > 3000) & (df["Kraj"] == "Niemcy")])

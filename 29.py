cena_chleb = 6.5
cena_sok = 4
cena_paczek = 5.50

ilosc_chleb = int(input("Ile kupujesz chleba ? "))
ilosc_sok = int(input("Ile kupujesz soku ? "))
ilosc_paczek = int(input("Ile kupujesz paczkow ? "))

cena_chelb = cena_chleb * ilosc_chleb
cena_sok = cena_sok * ilosc_sok
cena_paczek = cena_paczek * ilosc_paczek
cena_koncowa = cena_chelb + cena_sok + cena_paczek

print(f"""
Twoje zamówienie to:
        1. Chlebow - {ilosc_chleb}szt. - razem: {cena_chelb}
        2. Sokow - {ilosc_sok}szt. - razem: {cena_sok}
        3. Paczkow - {ilosc_paczek}szt. - razem: {cena_paczek}
        Razem do zaplaty: {cena_koncowa}
""")

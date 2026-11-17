import pandas as pd
import random
import json

print("Generowanie rozproszonych i 'brudnych' danych w silosach...")

# 1. ZTM - Udajemy stary system eksportujący do CSV z błędami jakości
ztm_dane = []
for _ in range(200):
    # Generujemy zepsute dane (np. tekst zamiast liczby, ujemne wartości, małe litery w nazwie linii)
    pasazerowie = random.choice([str(random.randint(10, 150)), "brak danych", "błąd czujnika", "-15"])
    linia = random.choice(["T-16", "A-169", "t-16 ", " a-169"])
    ztm_dane.append({"linia_autobusu": linia, "liczba_pasazerow_z_czujnika": pasazerowie})

pd.DataFrame(ztm_dane).to_csv('ztm_stary_system.csv', index=False)
print("-> Utworzono plik: ztm_stary_system.csv (Zawiera błędy, literówki i złe typy danych)")

# 2. MPU - Udajemy system mapowy zwracający pliki JSON, ale z brakami w GPS
mpu_dane = []
for _ in range(200):
    # Generujemy braki danych (30% szans na brak współrzędnych) i bałagan w nazwach
    lat = 52.4 + random.uniform(0, 0.08) if random.random() > 0.3 else None
    mpu_dane.append({
        "TYP_Zabudowy": random.choice(["wielorodzinna", "WIELORODZINNA", "Jednorodzinna "]),
        "wspolrzedna_lat": lat,
        "wspolrzedna_lon": 16.9 + random.uniform(0, 0.08) if lat else None
    })

with open('mpu_nowy_system.json', 'w', encoding='utf-8') as f:
    json.dump(mpu_dane, f, ensure_ascii=False, indent=2)
print("-> Utworzono plik: mpu_nowy_system.json (Różni się formatem, brakuje współrzędnych)")
print("Silosy wygenerowane pomyślnie!")
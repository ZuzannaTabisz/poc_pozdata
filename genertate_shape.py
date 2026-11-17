import json
import pandas as pd
import random
from datetime import datetime, timedelta

print("Generowanie zaawansowanych zbiorów...")

# 1. GeoJSON - Kształty (Poligony) dzielnic Poznania z danymi MPU
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"nazwa": "Stare Miasto", "typ": "Zabudowa Historyczna"},
            "geometry": {
                "type": "Polygon", # To rysuje obszar, a nie kropkę!
                "coordinates": [[[16.92, 52.41], [16.94, 52.41], [16.94, 52.39], [16.92, 52.39], [16.92, 52.41]]]
            }
        },
        {
            "type": "Feature",
            "properties": {"nazwa": "Jeżyce", "typ": "Zabudowa Mieszkaniowa"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[16.89, 52.42], [16.92, 52.42], [16.92, 52.40], [16.89, 52.40], [16.89, 52.42]]]
            }
        },
        {
            "type": "Feature",
            "properties": {"nazwa": "Wilda", "typ": "Tereny Poprzemysłowe"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[16.91, 52.39], [16.93, 52.39], [16.93, 52.37], [16.91, 52.37], [16.91, 52.39]]]
            }
        }
    ]
}
with open('poznan_strefy.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False)

# 2. ZTM - zbiór z osią czasu i specjalnie "wstrzykniętymi" błędami
ztm_dane = []
bazowa_data = datetime(2026, 11, 1) # Początek okresu
for i in range(500):
    data_pomiaru = bazowa_data + timedelta(hours=random.randint(0, 30*24))
    # Symulacja błędów: czasem czujnik zwraca liczbę ujemną, a czasem w ogóle nie działa (None)
    pasazerowie = random.choice([random.randint(10, 100), -5, -20, None])
    ztm_dane.append({
        "data_pomiaru": data_pomiaru.strftime("%Y-%m-%d %H:%M:%S"),
        "linia": random.choice(["T-16", "A-169", "T-15"]),
        "liczba_pasazerow": pasazerowie
    })
pd.DataFrame(ztm_dane).to_csv('ztm_czasowe.csv', index=False)

print("Gotowe: Utworzono poznan_strefy.geojson (Kształty) oraz ztm_czasowe.csv (Czas i Błędy).")
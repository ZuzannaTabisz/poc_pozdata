# Instrukcja uruchomienia PoC: POZ.DATA

## 1. Wymagane pakiety (Python)
- `duckdb` (Lokalny silnik analityczny)
- `pandas` (Przetwarzanie danych)
- `streamlit` (Aplikacja webowa i dashboard)
- `pydeck` (Silnik map przestrzennych 3D)
- `dbt-duckdb` (Narzędzie do Data Governance)

---

## 2. Komendy terminala (PowerShell)

### Krok 1: Instalacja środowiska (jednorazowo)
```powershell
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\python.exe' -m pip install duckdb pandas streamlit pydeck dbt-duckdb
```

### Krok 2

# 1. Wygenerowanie plików źródłowych (GeoJSON i CSV)
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\python.exe' generuj_zaawansowane.py

# 2. Uruchomienie pulpitu menedżerskiego w przeglądarce
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\python.exe' -m streamlit run dashboard.py

### Krok 3

# 1. Transformacja i czyszczenie danych
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\Scripts\dbt.exe' run --profiles-dir .

# 2. Audyt jakości danych (testy z pliku schema.yml)
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\Scripts\dbt.exe' test --profiles-dir .

# 3. Generowanie Katalogu Danych i grafu powiązań (Data Lineage)
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\Scripts\dbt.exe' docs generate --profiles-dir .

# 4. Udostępnienie Katalogu Danych w przeglądarce (localhost:8080)
& 'C:\Users\ZUZTAB\AppData\Local\Python\pythoncore-3.12-64\Scripts\dbt.exe' docs serve --profiles-dir .
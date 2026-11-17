import streamlit as st
import duckdb
import pydeck as pdk
import pandas as pd
import json

st.set_page_config(page_title="POZ.DATA - GIS & Data Explorer", layout="wide")
st.title("🚀 POZ.DATA - Kształty Przestrzenne i Wyszukiwarka")

tab1, tab2 = st.tabs(["🗺️ Mapa Przestrzenna (Poligony MPU)", "🔍 Wyszukiwarka Zbiorów (Data Explorer)"])

conn = duckdb.connect()

with tab1:
    st.subheader("Wizualizacja Obszarów (Strefy Planowania Przestrzennego)")
    st.write("Wgrywamy plik przestrzenny (GeoJSON) - zamiast pojedynczych punktów renderujemy całe dzielnice (kształty) i kolorujemy je.")
    
    # Ładujemy nasze kształty
    with open('poznan_strefy.geojson', 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
        
    # Tworzymy warstwę przestrzenną (PyDeck)
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_data,
        pickable=True,
        stroked=True,
        filled=True,
        get_fill_color="[30, 144, 255, 120]", # Niebieski z przezroczystością
        get_line_color="[255, 255, 255]",
        line_width_min_pixels=2,
    )
    
    # Ustawiamy kamerę na Poznań
    view_state = pdk.ViewState(latitude=52.40, longitude=16.92, zoom=11.5, pitch=30)
    
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{nazwa}\nTyp: {typ}"})
    st.pydeck_chart(r)

with tab2:
    st.subheader("Wewnętrzna Wyszukiwarka Danych (Data Catalog / Profiler)")
    st.write("System w locie skanuje zbiór, wyciąga zakres czasu i sprawdza zdrowie danych (alerty jakości).")
    
    wybrany_zbior = st.selectbox("Wybierz zbiór do analizy:", ["System Transportowy (ztm_czasowe.csv)", "System Planowania (poznan_strefy.geojson)"])
    
    if "ztm" in wybrany_zbior.lower():
        df = conn.execute("SELECT * FROM read_csv_auto('ztm_czasowe.csv')").df()
        
        # 1. WYCIĄGAMY RAMY CZASOWE
        df['data_pomiaru'] = pd.to_datetime(df['data_pomiaru'])
        min_data = df['data_pomiaru'].min()
        max_data = df['data_pomiaru'].max()
        
        st.markdown("### 📅 Metadane i Oś Czasu")
        col1, col2, col3 = st.columns(3)
        col1.metric("Liczba rekordów", len(df))
        col2.metric("Początek okresu", min_data.strftime("%Y-%m-%d %H:%M"))
        col3.metric("Koniec okresu", max_data.strftime("%Y-%m-%d %H:%M"))
        
        # 2. AUTOMATYCZNY AUDYT (WARNINGI)
        st.markdown("### ⚠️ Raport Jakości Danych")
        puste_wiersze = df['liczba_pasazerow'].isna().sum()
        ujemne_wiersze = (df['liczba_pasazerow'] < 0).sum()
        
        if puste_wiersze > 0:
            st.warning(f"**UWAGA:** Znaleziono {puste_wiersze} rekordów z pustą wartością (NULL). Sprawdź czujniki na bramkach!")
        if ujemne_wiersze > 0:
            st.error(f"**BŁĄD KRYTYCZNY:** Znaleziono {ujemne_wiersze} wpisów z UJEMNĄ liczbą pasażerów! Wstrzymano zasilanie hurtowni.")
            
        # 3. PODGLĄD DANYCH
        st.markdown("### 🔎 Podgląd surowych danych")
        st.dataframe(df.head(10))
        
    else:
        st.info("Zbiór MPU zawiera statyczne kształty geograficzne (brak osi czasu).")
        st.json(geojson_data['features'][0]['properties'])
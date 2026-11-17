SELECT
    UPPER(TRIM(linia_autobusu)) AS linia,
    TRY_CAST(liczba_pasazerow_z_czujnika AS INTEGER) AS liczba_pasazerow
FROM read_csv_auto('ztm_stary_system.csv')
WHERE TRY_CAST(liczba_pasazerow_z_czujnika AS INTEGER) > 0
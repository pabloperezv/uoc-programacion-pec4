''' Este modulo sirve para ejecutar la PEC 4 completa'''

import argparse
from embassaments.load_data import load_dataset
from embassaments.eda import display_head, display_columns, display_info
from embassaments.cleaning import (
    rename_columns,
    get_unique_stations,
    clean_station_names,
    filter_la_baells
)
from embassaments.temporal import (
    convert_to_datetime,
    sort_by_day,
    get_date_range,
    add_decimal_date_column,
    plot_volume,
    plot_smoothed_vs_original,
    calcula_periodos_sequia
)

PATH = "data/Quantitat_d_aigua_als_embassaments_de_les_Conques_Internes_de_Catalunya_20250607.csv"

def ejecutar_ejercicio_1():
    """Ejecuta el ejercicio 1: carga y exploración inicial del dataset."""
    print("Cargando dataset...")
    global df
    df = load_dataset(PATH)

    print("\nPrimeras 5 filas:")
    print(display_head(df))

    print("\nColumnas:")
    print(display_columns(df))

    print("\nInformación del DataFrame:")
    print(display_info(df))

def ejecutar_ejercicio_2():
    """Ejecuta el ejercicio 2: renombrado, limpieza y filtrado por embalse."""
    global df
    print("\nRenombrando columnas...")
    df = rename_columns(df)

    print("\nNombres únicos de embalses:")
    print(get_unique_stations(df))

    print("\nLimpiando nombres de embalses...")
    df = clean_station_names(df)
    print(get_unique_stations(df))

    print("\nFiltrando solo 'La Baells'...")
    global df_baells
    df_baells = filter_la_baells(df)
    print(df_baells.head())

def ejecutar_ejercicio_3():
    """Ejecuta el ejercicio 3: conversión temporal, orden y gráfico de volumen."""
    global df_baells
    df_baells = convert_to_datetime(df_baells)
    df_baells = sort_by_day(df_baells)

    fecha_min, fecha_max = get_date_range(df_baells)
    print(f"\nFecha más antigua: {fecha_min.date()} — Fecha más reciente: {fecha_max.date()}")

    df_baells = add_decimal_date_column(df_baells)
    print(df_baells[['dia', 'dia_decimal']].head())

    ruta_salida = "img/labaells_pablo_perez-verdugo.png"
    plot_volume(df_baells, ruta_salida)
    print(f"\nGráfico guardado en: {ruta_salida}")

def ejecutar_ejercicio_4():
    """Ejecuta el ejercicio 4: suavizado de la serie temporal."""
    ruta_salida2 = "img/labaells_smoothed_pablo_perez-verdugo.png"
    plot_smoothed_vs_original(df_baells, ruta_salida2)
    print(f"\nGráfico suavizado guardado en: {ruta_salida2}")

def ejecutar_ejercicio_5():
    """Ejecuta el ejercicio 5: detección de periodos de sequía."""
    periodos_sequia = calcula_periodos_sequia(df_baells)

    print("\nPeriodos de sequía detectados (volumen < 60%):")
    for p in periodos_sequia:
        print(f" - Desde {p[0]} hasta {p[1]}")

def parse_args():
    """Parsea los parametros -ex --ejercicio -h --help"""
    parser = argparse.ArgumentParser(
        description="PEC4 - Embassaments: ejecuta los ejercicios del 1 al 5"
    )
    parser.add_argument(
        "-ex", "--ejercicio", type=int, choices=range(1, 6),
        help="Ejecutar ejercicios hasta el número especificado (1-5)"
    )
    return parser.parse_args()

def main():
    """Ejecuta los ejercicios en funcion del parametro -ex --ejercicio"""
    args = parse_args()
    hasta = args.ejercicio or 5

    if hasta >= 1:
        ejecutar_ejercicio_1()
    if hasta >= 2:
        ejecutar_ejercicio_2()
    if hasta >= 3:
        ejecutar_ejercicio_3()
    if hasta >= 4:
        ejecutar_ejercicio_4()
    if hasta >= 5:
        ejecutar_ejercicio_5()


if __name__ == "__main__":
    main()

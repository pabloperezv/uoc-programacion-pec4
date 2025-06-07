''' Este modulo sirve para realizar las transformaciones de la columna temporal y plotear distintas series temporales'''
import datetime
import os
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import pandas as pd

def convert_to_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte la columna 'dia' al tipo datetime."""
    df['dia'] = pd.to_datetime(df['dia'], dayfirst=True, errors='coerce')
    return df

def sort_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """Ordena el dataframe por la columna 'dia' en orden ascendente."""
    return df.sort_values('dia').reset_index(drop=True)

def get_date_range(df: pd.DataFrame) -> tuple:
    """Devuelve la fecha más antigua y la más reciente del dataframe."""
    return df['dia'].min(), df['dia'].max()

def to_year_fraction(date: datetime.datetime) -> float:
    """Convierte una fecha datetime a su valor decimal en años."""
    year_start = datetime.datetime(date.year, 1, 1)
    next_year_start = datetime.datetime(date.year + 1, 1, 1)
    year_elapsed = (date - year_start).total_seconds()
    year_duration = (next_year_start - year_start).total_seconds()
    return date.year + year_elapsed / year_duration

def add_decimal_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """Crea la columna 'dia_decimal' a partir de 'dia'."""
    df['dia_decimal'] = df['dia'].apply(to_year_fraction)
    return df

def plot_volume(df: pd.DataFrame, output_path: str) -> None:
    """Genera y guarda un gráfico de la evolución del volumen del embalse."""
    plt.figure(figsize=(10, 5))
    plt.plot(df['dia'], df['nivell_perc'], marker='o', linestyle='-', color='blue')
    plt.title('Evolución del volumen de La Baells - Pablo Perez Verdugo')
    plt.xlabel('Fecha')
    plt.ylabel('Volumen (%)')
    plt.grid(True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def plot_smoothed_vs_original(df: pd.DataFrame, output_path: str) -> None:
    """
    Aplica suavizado con savgol_filter y genera un gráfico con el volumen original y suavizado.
    """

    y_original = df['nivell_perc'].fillna(method='ffill').fillna(method='bfill').values
    x_values = df['dia'].values

    window_length  = 1500 if len(y_original) >= 1500 else (len(y_original) // 2) * 2 + 1
    y_smooth = savgol_filter(y_original, window_length , 3)

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 8)
    ax.plot(x_values, y_smooth, color='blue', label='Suavizado', linewidth=3)
    ax.plot(x_values, y_original, color='red', alpha=0.5, label='Original')
    plt.title('Evolución volumen embalse La Baells - Pablo Perez Verdugo')
    plt.xlabel('Fecha')
    plt.ylabel('Volumen (%)')
    ax.legend()
    plt.grid(True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

def calcula_periodos_sequia(df: pd.DataFrame, threshold: float = 60.0) -> list:
    """
    Calcula los periodos de sequía.

    Parametros:
        df (pd.DataFrame): DataFrame con las columnas 'dia_decimal' y 'nivell_perc'.
        threshold (float): Umbral de sequía (%).

    Devuelve:
        List[List[float]]: Lista de periodos de sequía como pares [inicio, fin].
    """

    y = df['nivell_perc'].fillna(method='ffill').fillna(method='bfill').values

    # Aplicamos suavizado
    y_smooth = savgol_filter(y, 1500, 3)

    below_threshold = y_smooth < threshold
    dia_decimal = df['dia_decimal']

    periods = []
    start = None

    for i in range(len(below_threshold)):
        if below_threshold[i] and start is None:
            start = dia_decimal.iloc[i]
        elif not below_threshold[i] and start is not None:
            end = dia_decimal.iloc[i - 1]
            periods.append([round(start, 2), round(end, 2)])
            start = None

    if start is not None:
        periods.append([round(start, 2), round(dia_decimal.iloc[-1], 2)])

    return periods

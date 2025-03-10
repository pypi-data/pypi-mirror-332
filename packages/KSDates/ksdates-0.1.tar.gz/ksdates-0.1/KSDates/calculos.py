# KSDates/calculos.py

from datetime import datetime, timedelta

def diferencia_fechas(fecha_1: str, fecha_2: str, formato: str) -> str:
    """
    Calcula la diferencia entre dos fechas en formato 'dd/mm/yyyy'.
    Devuelve la diferencia en días.
    """
    fecha_1_obj = datetime.strptime(fecha_1, formato)
    fecha_2_obj = datetime.strptime(fecha_2, formato)
    diferencia = abs(fecha_1_obj - fecha_2_obj)
    return str(diferencia.days)  # Devuelve la diferencia en días

def fecha_futura(fecha_base: str, dias: int, formato: str) -> str:
    """
    Genera una fecha futura a partir de una fecha base añadiendo un número de días.
    """
    fecha_base_obj = datetime.strptime(fecha_base, formato)
    fecha_futura = fecha_base_obj + timedelta(days=dias)
    return fecha_futura.strftime(formato)

def fecha_pasada(fecha_base: str, dias: int, formato: str) -> str:
    """
    Genera una fecha pasada a partir de una fecha base restando un número de días.
    """
    fecha_base_obj = datetime.strptime(fecha_base, formato)
    fecha_pasada = fecha_base_obj - timedelta(days=dias)
    return fecha_pasada.strftime(formato)

  
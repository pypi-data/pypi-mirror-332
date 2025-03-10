# KSDates/fechas.py

from datetime import datetime

def convertir_fecha(fecha_str: str, formato_entrada: str, formato_salida: str) -> str:
    """
    Convierte una fecha desde un formato de entrada a un formato de salida especificado.
    Ejemplo: convertir_fecha("2025-03-09", "%Y-%m-%d", "%d/%m/%Y")
    """
    try:
        fecha_obj = datetime.strptime(fecha_str, formato_entrada)
        return fecha_obj.strftime(formato_salida)
    except ValueError:
        raise ValueError("Formato de fecha inválido")

def es_fecha_valida(fecha_str: str, formato: str) -> bool:
    """
    Verifica si una fecha es válida según el formato especificado.
    """
    try:
        datetime.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False  

# KAS - Librería para manejo de fechas y horarios en Python

`KAS` es una librería simple y eficiente para trabajar con fechas y horarios en Python. Permite convertir fechas entre diferentes formatos, calcular la diferencia entre dos fechas, y generar fechas futuras o pasadas a partir de una fecha base. Es ideal para aplicaciones que gestionan plazos, eventos, vencimientos y otras tareas relacionadas con fechas.

# USO
1. Convertir fechas entre diferentes formatos

from KAS.fechas import convertir_fecha

# Convertir de formato "dd/mm/yyyy" a "yyyy-mm-dd"
fecha_convertida = convertir_fecha("09/03/2025", "%d/%m/%Y", "%Y-%m-%d")
print(fecha_convertida)  # Salida: 2025-03-09


2. Verificar si una fecha es válida

from KAS.fechas import es_fecha_valida

es_valida = es_fecha_valida("09/03/2025", "%d/%m/%Y")
print(es_valida)  # Salida: True


3. Calcular la diferencia entre dos fechas

from KAS.calculos import diferencia_fechas

diferencia = diferencia_fechas("09/03/2025", "01/03/2025", "%d/%m/%Y")
print(diferencia)  # Salida: 8


4. Generar una fecha futura o pasada

from KAS.calculos import fecha_futura, fecha_pasada

# Generar una fecha futura (10 días después)
fecha_futura_10_dias = fecha_futura("09/03/2025", 10, "%d/%m/%Y")
print(fecha_futura_10_dias)  # Salida: 19/03/2025

# Generar una fecha pasada (10 días antes)
fecha_pasada_10_dias = fecha_pasada("09/03/2025", 10, "%d/%m/%Y")
print(fecha_pasada_10_dias)  # Salida: 27/02/2025



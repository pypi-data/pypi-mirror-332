# tests/test_calculos.py

import unittest
from KSDates.calculos import diferencia_fechas, fecha_futura, fecha_pasada

class TestCalculos(unittest.TestCase):
    def test_diferencia_fechas(self):
        diferencia = diferencia_fechas("09/03/2025", "01/03/2025", "%d/%m/%Y")
        self.assertEqual(diferencia, "8")

    def test_fecha_futura(self):
        fecha = fecha_futura("09/03/2025", 10, "%d/%m/%Y")
        self.assertEqual(fecha, "19/03/2025")

    def test_fecha_pasada(self):
        fecha = fecha_pasada("09/03/2025", 10, "%d/%m/%Y")
        self.assertEqual(fecha, "27/02/2025")

if __name__ == "__main__":
    unittest.main() 

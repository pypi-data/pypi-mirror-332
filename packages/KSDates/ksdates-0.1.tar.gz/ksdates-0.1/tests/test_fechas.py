# tests/test_fechas.py

import unittest
from KSDates.fechas import convertir_fecha, es_fecha_valida

class TestFechas(unittest.TestCase):
    def test_convertir_fecha(self):
        fecha = convertir_fecha("2025-03-09", "%Y-%m-%d", "%d/%m/%Y")
        self.assertEqual(fecha, "09/03/2025")

    def test_es_fecha_valida(self):
        self.assertTrue(es_fecha_valida("09/03/2025", "%d/%m/%Y"))
        self.assertFalse(es_fecha_valida("2025-03-09", "%d/%m/%Y"))

if __name__ == "__main__":
    unittest.main() 

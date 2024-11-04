import unittest
from src.calculations import calcular_correntes

class TestCalcularCorrentes(unittest.TestCase):
    def test_circuito_basico(self):
        nos = ['A', 'B', 'C']
        elementos = {
            ('A', 'B', 'R'): 100,
            ('B', 'C', 'R'): 200,
            ('A', 'C', 'V'): 10
        }
        tensoes_nos, correntes_elementos = calcular_correntes(nos, elementos)
        self.assertAlmostEqual(tensoes_nos['A'], 10.0, places=2)
        self.assertAlmostEqual(tensoes_nos['B'], 6.6667, places=4)
        self.assertEqual(tensoes_nos['C'], 0.0)

if __name__ == '__main__':
    unittest.main()

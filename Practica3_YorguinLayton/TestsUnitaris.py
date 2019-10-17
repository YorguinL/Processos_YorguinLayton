import unittest
from EquacioPrimerGrau import EquacioPrimerGrau1

class TestsUnitaris(unittest.TestCase):
    def test_positiu(self):
        eq = EquacioPrimerGrau1("2x + 4 = 10")
        self.assertEqual(eq.calcula(),3.0)

    def testincorrecte(self):
        eq = EquacioPrimerGrau1("2x / 3 = 7")
        self.assertEqual(eq.calcula(),"Operador no valid: " + eq.operador1)
        self.assertIsInstance(eq.operador1, basestring)

    def test_negatiu(self):
        eq = EquacioPrimerGrau1("2x - 3 = 7")
        self.assertEqual(eq.calcula(),5)

    def test_float(self):
        eq = EquacioPrimerGrau1("2.3x - 8.4 = 9.8")
        self.assertEqual(eq.calcula(),7.913043478260872)

    def test_caracter_erroni(self):
        eq = EquacioPrimerGrau1("2x - p = 7")
        self.assertEqual(eq.calcula(),"l'equacio conte caracter no calculables: "+eq.b)

    def test_fromat_erroni(self):
        eq = EquacioPrimerGrau1("3 - 2x = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")


if __name__ == "__main__":
    unittest.main()

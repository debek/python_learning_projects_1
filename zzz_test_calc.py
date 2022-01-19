import unittest
import zzz_calc

class testCalc(unittest.TestCase):

    def test_suma(self):
        wynik = zzz_calc.suma(10,5)
        self.assertEqual(wynik, 15)

    def test_roznica(self):
        wynik = zzz_calc.roznica(10,5)
        self.assertEqual(wynik, 5)

    def test_iloczyn(self):
        wynik = zzz_calc.iloczyn(5,10)
        self.assertEqual(wynik, 50)

    def test_iloraz(self):
        wynik = zzz_calc.iloraz(10,5)
        self.assertEqual(wynik, 2)

    def test_iloraz2(self):
        wynik = zzz_calc.iloraz(10,0)
        self.assertEqual(wynik, "Nie dzielimy przez 0")

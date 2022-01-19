import unittest
from contact import *

class testContact(unittest.TestCase):

    contact1 = contact("Adam", "Nowak")
    contact2 = contact("Tomasz", "Kowalski")

    def test_email(self):
        wynik = self.contact1.email()
        wynik2 = self.contact2.email()

        self.assertEqual(wynik, "Adam_Nowak@firma.pl")
        self.assertEqual(wynik2, "Tomasz_Kowalski@firma.pl")

    def test_przedstawSie(self):
        wynik = self.contact1.przedstawSie()
        wynik2 = self.contact2.przedstawSie()

        self.assertEqual(wynik, "Adam Nowak")
        self.assertEqual(wynik2, "Tomasz Kowalski")

import unittest
from unittest.mock import patch

def additionner(a, b):
    return a+b


def conversion_nombre():
    num_str = input("Rentrez un nombre : ")
    return int(num_str)


class TestsUnitaireDemo(unittest.TestCase):
    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_additionner_nombres_positifs(self):
        print("test_additionner1")
        self.assertEqual(additionner(5, 10), 15)
        self.assertEqual(additionner(6, 10), 16)
        self.assertEqual(additionner(6000, 5), 6005)

    def test_additionner_nombres_negatifs(self):
        print("test_additionner2")
        self.assertEqual(additionner(-6, -10), -16)

    def test_conversion_nombre_valide(self):
        with patch("builtins.input", return_value="10"):
            self.assertEqual(conversion_nombre(), 10)
        with patch("builtins.input", return_value="100"):
            self.assertEqual(conversion_nombre(), 100)
   
    def test_conversion_entree_invalide(self):       
        with patch("builtins.input", return_value="abcd"):
            self.assertRaises(ValueError, conversion_nombre)


unittest.main()
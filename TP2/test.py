# python -m unittest test.py
import unittest
from utils import *;

class Testing(unittest.TestCase):
    def test_testerSiIdentifiantExist(self):
        listeDesProduits = {1:{"Nom":"Banane","Prix":4.0,"Quantite":0}, 2:{"Nom":"Pomme","Prix":2.0,"Quantite":0}, 3:{"Nom":"Orange","Prix":1.5,"Quantite":0}, 4:{"Nom":"Poire","Prix":3.0,"Quantite":0}}
        a = testerSiIdentifiantExist(1, listeDesProduits)
        b = True
        self.assertEqual(a, b)

    def test_calculerTotal(self):
        listeDesProduits = {1:{"Nom":"Banane","Prix":4.0,"Quantite":4}, 2:{"Nom":"Pomme","Prix":2.0,"Quantite":2}, 3:{"Nom":"Orange","Prix":1.5,"Quantite":0}, 4:{"Nom":"Poire","Prix":3.0,"Quantite":0}}
        a = calculerTotal(listeDesProduits)
        b = 20.0 
        self.assertEqual(a, b)

    def test_calculerTotalTTC(self):
        a = calculerTotalTTC(20.0)
        b = 24.0
        self.assertEqual(a, b)

    def test_calculerRemise_sup(self):
        a = calculerRemise(0.95, 200, 450)
        b = 427.5
        self.assertEqual(a, b)

    def test_calculerRemise_inf(self):
        a = calculerRemise(0.95, 200, 190)
        b = 190.0
        self.assertEqual(a, b)

    def test_calculerRemise_equal(self):
        a = calculerRemise(0.95, 200, 200)
        b = 200.0
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
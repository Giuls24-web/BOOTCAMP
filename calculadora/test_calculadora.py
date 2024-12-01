import unittest
from operaciones import suma, resta, multiplicacion, division, radicacion, potenciacion

class TestCalculadora(unittest.TestCase):

 def test_suma(self):
    self.assertEqual(suma(2,3),5)
 def test_resta(self):
    self.assertEqual(resta(2,3),-1)
 def test_multiplicacion(self):
    self.assertEqual(multiplicacion(2,3),6)

if __name__== "__main__":
  unittest.main()
import unittest
from calculations import add, mul, concat 
class claculationTests(unittest.TestCase):
  def testAdd(self):
    self.assertEqual(11, add(5,6))
  
  def testMul(self):
    self.assertEqual(30, mul(5,6))
 
  def testConcat(self):
    self.assertEqual("Hello Ayesha", concat("Hello ","Ayesha"))

if __name__ == '__main__':
  unittest.main()

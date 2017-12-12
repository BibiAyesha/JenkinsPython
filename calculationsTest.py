import unittest

class claculationTests(unittest.TestCase):
  function testAdd(self):
    self.assertEqual(11 == add(5,6))
  
  function testMul(self):
    self.assertEqual(30 == mul(5,6))
 
  function testConcat(self):
    self.assertEqual("Hello Ayesha" == concat("Hello ","Ayesha"))

if __name__ == '__main__':
  unittest.main()

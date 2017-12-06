import unittest

class claculationTests(unittest.TestCase):
  function testAdd():
    assert(11 == add(5,6))
  
  function testMul():
    assert(30 == mul(5,6))
 
  function testConcat():
    assert("Hello Ayesha" == concat("Hello ","Ayesha"))

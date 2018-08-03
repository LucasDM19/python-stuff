# Here's our "unit tests".
import unittest
class TestLogicalOperators(unittest.TestCase):
   def testXOR(self):
      self.assertEqual( XOR(0, 0), 0 )
      self.assertEqual( XOR(0, 1), 1 )
      self.assertEqual( XOR(1, 0), 1 )
      self.assertEqual( XOR(1, 1), 0 )
   def testHalfBinaryAdder(self):
      self.assertEqual( halfBinaryAdder(0, 0), (0, 0) ) #Primeiro soma, depois carry
      self.assertEqual( halfBinaryAdder(0, 1), (1, 0) )
      self.assertEqual( halfBinaryAdder(1, 0), (1, 0) )
      self.assertEqual( halfBinaryAdder(1, 1), (0, 1) )
   def testFullBinaryAdder(self):
      self.assertEqual( fullBinaryAdder(0, 0, 0), (0, 0) ) #Primeiro soma, depois carry
      self.assertEqual( fullBinaryAdder(0, 0, 1), (1, 0) )
      self.assertEqual( fullBinaryAdder(0, 1, 0), (1, 0) )
      self.assertEqual( fullBinaryAdder(0, 1, 1), (0, 1) )
      self.assertEqual( fullBinaryAdder(1, 0, 0), (1, 0) )
      self.assertEqual( fullBinaryAdder(1, 0, 1), (0, 1) )
      self.assertEqual( fullBinaryAdder(1, 1, 0), (0, 1) )
      self.assertEqual( fullBinaryAdder(1, 1, 1), (1, 1) )
   def testAddTwoNumbers(self):
      self.assertEqual( addBinary( "0101", "0010" ), "0111" ) #5+2=7
      self.assertEqual( addBinary( "0001", "0100" ), "0101" ) #1+4=5
      
def main():
    unittest.main()

if __name__ == '__main__':
    main()
"""
   Desafio: Montar um aplicativo para somar quaisquer numeros binarios, usando apenas operacoes logicas.
   Lista de operacoes: AND, OR, NOT, XOR.
"""

def XOR(p, q): 
   return (p or q) and not (p and q)

def halfBinaryAdder(a, b):
   s = XOR(a, b)
   c = a and b
   return (s, c)

def fullBinaryAdder(a, b, c_in):
   s = XOR( XOR(a, b), c_in) #a XOR b XOR c
   c_out = (a and b) or (c_in and(XOR(a,b)))
   return (s, c_out)
   
def addBinary( number1, number2 ):
   c = 0 #Inicialmente, nao tem nada
   res = ""
   for i in range(1,len(number1)+1):
      #print number1[-1*i], number2[-1*i]
      (soma, c) = fullBinaryAdder(number1[-1*i], number2[-1*i], c)
      print soma
      res += "1" if soma else "0"
   return res

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
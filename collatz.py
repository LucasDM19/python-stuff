"""
	31/08/2015
	Vi uma tirinha sobre essa doideira da hipótese de Collatz.
	Tentei formular essa função, e outra que a chama, um número por vez
"""
def collatz( n ):
   #If it is even, divide bo two
   if( n % 2 == 0 ) : return n/2
   #If it is odd, mutiply by three and add one
   if( n % 2 == 1 ) : return 3*n+1

def collatizator( number ):
   if number <= 0: return "WTF!"
   res = ""
   while( number != 1 ):
      res += str(number) + ", "
      number = collatz( number )
   return res + "1"

   
"""
	Hora de testar um pouco
"""

import unittest

class TestCollatz(unittest.TestCase):
	def testcollatz_1(self):
		self.assertEqual( collatz(1), 4)
	def testcollatz_2(self):
		self.assertEqual( collatz(2), 1)
	def testcollatz_3(self):
		self.assertEqual( collatz(3), 10)

class TestCollatizator(unittest.TestCase):
	def testcollatizator_10(self):
		self.assertEqual( collatizator(10), "10, 5, 16, 8, 4, 2, 1")		
	def testcollatizator_99(self):
		self.assertEqual( collatizator(99), "99, 298, 149, 448, 224, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1")
		
def main():
    unittest.main()
		
if __name__ == '__main__':
	print ">>A little bit of testing, in the sun"
	main()
		
	#print ">>A little bit of printing, all night long"
	#for n in range(100):
	#	print collatizator( n ) 
   
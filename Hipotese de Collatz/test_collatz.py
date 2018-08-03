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
   
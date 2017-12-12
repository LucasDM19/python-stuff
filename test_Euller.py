"""
   Arquivo com todos os testes do Project Euller.
   Assim os problemas sempre tem uma garantia de funcionarem conforme o especificado.
   Arquivo separado para melhor legibildiade.
"""
import unittest
from Euller import * #Classe a ser testada - Chama TUDO

# Below are our "units".
# as seen on http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html
# Actually, i put it in a separated file.

def main():
    unittest.main()

# Here's our "unit tests".
class TestProblem1(unittest.TestCase):
   #Teste 0001
   def testProblem1_1(self):
      self.assertEqual( problem1(10), 23 ) #we get 3, 5, 6 and 9. The sum of these multiples is 23.
   #Teste 0002
   def testProblem1_2(self):
      self.assertEqual( problem1(1000), 233168 ) #Find the sum of all the multiples of 3 or 5 below 1000

class TestProblem2(unittest.TestCase):
   #Teste 0003
   def testFibonacci_0(self):
      self.assertEqual( fibonacci(0), 0 )
   #Teste 0004
   def testFibonacci_1(self):
      self.assertEqual( fibonacci(1), 1 )
   #Teste 0005
   def testFibonacci_2(self):
      self.assertEqual( fibonacci(2), 1 )
   #Teste 0006
   def testFibonacci_3(self):
      self.assertEqual( fibonacci(3), 2 )
   #Teste 0007
   def testFibonacci_4(self):
      self.assertEqual( fibonacci(4), 3 )
   #Teste 0008
   def testFibonacci_5(self):
      self.assertEqual( fibonacci(5), 5 )
   #Teste 0009
   def testFibonacci_6(self):
      self.assertEqual( fibonacci(6), 8 )
   #Teste 0010
   def testFibonacci_7(self):
      self.assertEqual( fibonacci(7), 13 )
   #Teste 0011
   def testFibonacci_8(self):
      self.assertEqual( fibonacci(8), 21 )
   #Teste 0012
   def testFibonacci_9(self):
      self.assertEqual( fibonacci(9), 34 )
   #Teste 0013
   def testFibonacci_10(self):
      self.assertEqual( fibonacci(10), 55 )
   #Teste 0014
   def testProblem2_1(self):
      self.assertEqual( problem2(4000000), 4613732 )
      
class TestProblem3(unittest.TestCase):
   #Teste 0015
   def testEratosthenes_1(self):
      self.assertEqual( sieveOfEratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] )
   #Teste 0016
   def testPrimeFactors_1(self):
      self.assertEqual( primeFactors(13195), [5, 7, 13, 29] ) #The prime factors of 13195 are 5, 7, 13 and 29.
   #Teste 0017
   def testProblem3_1(self):
      self.assertEqual( problem3(600851475143), 6857 )

class TestProblem4(unittest.TestCase):
   #Teste 0018
   def testIsPalindromicNumber_1(self):
      self.assertEqual( isPalindromicNumber(1), True )
   #Teste 0019
   def testIsPalindromicNumber_2(self):
      self.assertEqual( isPalindromicNumber(16), False )
   #Teste 0020
   def testIsPalindromicNumber_3(self):
      self.assertEqual( isPalindromicNumber(22), True )
   #Teste 0021
   def testIsPalindromicNumber_4(self):
      self.assertEqual( isPalindromicNumber(9009), True ) #The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
   #Teste 0022
   def testIsPalindromicNumber_5(self):
      self.assertEqual( isPalindromicNumber(1234), False )
   #Teste 0023
   def testProblem4_1(self):
      self.assertEqual( problem4(2), 9009 )
   #Teste 0024
   def testProblem4_2(self):
      self.assertEqual( problem4(3), 906609 ) #Demora DEMAIS

class TestProblem5(unittest.TestCase):
   """ Nao eh mais necessario testar isso
   def testFactorial_1(self):
      self.assertEqual( factorial(1), 1)
   def testFactorial_2(self):
      self.assertEqual( factorial(5), 120)
   """
   def testProblem5_1(self):
      self.assertEqual( problem5(10), 2520) # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
   def testProblem5_2(self):
      self.assertEqual( problem5(20), 232792560)

class TestProblem6(unittest.TestCase):
   def testSumOfSquares_10(self):
      self.assertEqual( sum_of_squares(10), 385)
   def testSquareOfSum_10(self):
      self.assertEqual( squares_of_sum(10), 3025)
   def testProblem6_10(self):
		self.assertEqual( problem6(10), 2640)
   def testProblem6_100(self):
		self.assertEqual( problem6(100), 25164150)

class TestProblem7(unittest.TestCase):
   def testProblem7_6(self):
		self.assertEqual( problem7(6), 13)
   def testProblem6_100001(self):
		self.assertEqual( problem7(10001), 104743)

class TestProblem8(unittest.TestCase):
   def testProblem8_4(self):
      hugeMotherfuckerNumber="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
      self.assertEqual( problem8(hugeMotherfuckerNumber, 4), 5832)
   def testProblem8_13(self):
      hugeMotherfuckerNumber="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
      self.assertEqual( problem8(hugeMotherfuckerNumber, 13), 23514624000)
      
if __name__ == '__main__':
    main()
      
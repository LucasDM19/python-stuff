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

def main():
    print("Rode os testes!")
		
if __name__ == '__main__':
	main()   
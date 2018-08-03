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
      (soma, cn) = fullBinaryAdder(number1[-1*i], number2[-1*i], c)
      print("Op=",number1,number2, ", Soma=",soma, ", cn=", cn, ", n1=", number1[-1*i], ", n2=", number2[-1*i], ", c=", c)
      c = cn
      res += "1" if soma else "0"
   return res

def main():
    print("Rode os testes!")
   
if __name__ == '__main__':
    main()
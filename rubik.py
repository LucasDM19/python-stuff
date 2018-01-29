#Classe para as cores do cubo mágico.
#Função clássica é azul, verde, amarelo, branco, vermelho e laranja
#As cores que estão nas faces opostas do cubo são: amarelo/branco, vermelho/laranja e azul/verde.
class Color :
   CoresValidas = range(6)
   AZUL, VERDE, AMARELO, BRANCO, VERMELHO, LARANJA = CoresValidas
   def __init__(self, value, id):
      if value in self.CoresValidas :
         self.value = value
         self.id = id
      #TODO: raise invalid value exception
   def getValue(self):
      return self.value
   def __str__(self):
      return str( self.id )

class rubikCube:
   #cubo = Color[6][3][3]
   cubo = [[[Color for x in range(6)] for y in range(3)] for z in range(3)]

def rotacionaFace(face):
   #face = [[Color(0, 3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] 
   print face[0][0],"|",face[0][1],"|",face[0][2]
   print face[1][0],"|",face[1][1],"|",face[1][2]
   print face[2][0],"|",face[2][1],"|",face[2][2]
   print "_________________________________"

   #Tentarei agora rotacionar a tal face
   from copy import deepcopy
   face2 = deepcopy(face) #aquela Dolly clonada

   for i in range(MAX_LINE):
      for j in range(MAX_COLUMN):
         face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
   #face2 = [face[2-j][i] for i in range(3) for j in range(3)] 
   face = face2
   print face[0][0],"|",face[0][1],"|",face[0][2]
   print face[1][0],"|",face[1][1],"|",face[1][2]
   print face[2][0],"|",face[2][1],"|",face[2][2]
   print "_________________________________"
   return face
#c = Color(2)
#print c

#depois isso vira objeto
MAX_FACES = 6
MAX_LINE = 3
MAX_COLUMN = 3
cubo = [[[Color(0, 9*z+3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] for z in range(MAX_FACES)]
print cubo[4][1][1]
cubo[0] = rotacionaFace( cubo[0] ) 
cubo[0] = rotacionaFace( cubo[0] ) 
cubo[0] = rotacionaFace( cubo[0] ) 
cubo[0] = rotacionaFace( cubo[0] ) 

"""
Testar se:
1) Color instanciada com uma cor continua com aquela cor
2) Se Color errada gera a exception
3) print face[2][1] tem de ser 7, sendo face = 0 
4) face normal e rotacionada. (0 1 2 3 4 5 6 7 8) vira (6 3 0 7 4 1 8 5 2)
5) rotacionar 4 vezes teria de deixar igual no inicio
"""
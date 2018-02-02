﻿#Classe para as cores do cubo mágico.
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
   MAX_FACES = 6
   MAX_LINE = 3
   MAX_COLUMN = 3
   cubo = [[[Color(0, 9*z+3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] for z in range(MAX_FACES)]
   
   def __str__(self):
      BLANK_LINE = "      "
      FILLER = "-----------------------------" 
      line1  = BLANK_LINE + str(self.cubo[1][0][0])+"|"+str(self.cubo[1][0][1])+"|"+str(self.cubo[1][0][2]) + "\n"
      line2  = BLANK_LINE + str(self.cubo[1][1][0])+"|"+str(self.cubo[1][1][1])+"|"+str(self.cubo[1][1][2]) + "\n"
      line3  = BLANK_LINE + str(self.cubo[1][2][0])+"|"+str(self.cubo[1][2][1])+"|"+str(self.cubo[1][2][2]) + "\n"
      line4  = FILLER + "\n"
      line5  = str(self.cubo[5][0][0])+"|"+str(self.cubo[5][0][1])+"|"+str(self.cubo[5][0][2])+"|"+str(self.cubo[0][0][0])+"|"+str(self.cubo[0][0][1])+"|"+str(self.cubo[0][0][2])+"|"+str(self.cubo[2][0][0])+"|"+str(self.cubo[2][0][1])+"|"+str(self.cubo[2][0][2])+"|"+str(self.cubo[3][0][0])+"|"+str(self.cubo[3][0][1])+"|"+str(self.cubo[3][0][2]) + "\n"
      line6  = str(self.cubo[5][1][0])+"|"+str(self.cubo[5][1][1])+"|"+str(self.cubo[5][1][2])+"|"+str(self.cubo[0][1][0])+"|"+str(self.cubo[0][1][1])+"|"+str(self.cubo[0][1][2])+"|"+str(self.cubo[2][1][0])+"|"+str(self.cubo[2][1][1])+"|"+str(self.cubo[2][1][2])+"|"+str(self.cubo[3][1][0])+"|"+str(self.cubo[3][1][1])+"|"+str(self.cubo[3][1][2]) + "\n"
      line7  = str(self.cubo[5][2][0])+"|"+str(self.cubo[5][2][1])+"|"+str(self.cubo[5][2][2])+"|"+str(self.cubo[0][2][0])+"|"+str(self.cubo[0][2][1])+"|"+str(self.cubo[0][2][2])+"|"+str(self.cubo[2][2][0])+"|"+str(self.cubo[2][2][1])+"|"+str(self.cubo[2][2][2])+"|"+str(self.cubo[3][2][0])+"|"+str(self.cubo[3][2][1])+"|"+str(self.cubo[3][2][2]) + "\n"
      line8  = FILLER + "\n"
      line9  = BLANK_LINE + str(self.cubo[4][0][0])+"|"+str(self.cubo[4][0][1])+"|"+str(self.cubo[4][0][2]) + "\n"
      line10 = BLANK_LINE + str(self.cubo[4][1][0])+"|"+str(self.cubo[4][1][1])+"|"+str(self.cubo[4][1][2]) + "\n"
      line11 = BLANK_LINE + str(self.cubo[4][2][0])+"|"+str(self.cubo[4][2][1])+"|"+str(self.cubo[4][2][2]) + "\n"
      return line1+line2+line3+line4+line5+line6+line7+line8+line9+line10+line11
      
   #Rotaciono o cubo no sentido horário
   def rotacionaFace(self,indice):
      face = self.cubo[indice]
      #Tentarei agora rotacionar a tal face
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      
      #Rotacionando os vizinhos
      VIZINHOS = [[1, 4, 2, 5],
                  [4, 4, 2, 5],
                  [1, 4, 3, 0],
                  [1, 4, 5, 2],
                  [0, 1, 2, 5],
                  [1, 4, 0, 3], ]
      ACIMA, ABAIXO, DIREITA, ESQUERDA = range(4)
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[VIZINHOS[indice][ACIMA]][2][i] = self.cubo[VIZINHOS[indice][ESQUERDA]][MAX_LINE-1-i][2] #ACIMA
         cubo2[VIZINHOS[indice][DIREITA]][i][0] = self.cubo[VIZINHOS[indice][ACIMA]][2][i]            #DIREITA
         cubo2[VIZINHOS[indice][ABAIXO]][0][i] = self.cubo[VIZINHOS[indice][DIREITA]][MAX_LINE-1-i][0] #ABAIXO
         cubo2[VIZINHOS[indice][ESQUERDA]][i][2] = self.cubo[VIZINHOS[indice][ABAIXO]][0][i]            #ESQUERDA
      self.cubo = cubo2 #desclonou
      self.cubo[indice] = face2
   
#c = Color(2)
#print c

#depois isso vira objeto
MAX_FACES = 6
MAX_LINE = 3
MAX_COLUMN = 3
cubo = [[[Color(0, 9*z+3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] for z in range(MAX_FACES)]
#print cubo[4][1][1]

r = rubikCube()
print r
r.rotacionaFace(0)
#r.rotacionaFace(0)
#r.rotacionaFace(0)
#r.rotacionaFace(0)
print r


#Rotacionando 4 vezes
#cubo[0] = rotacionaFace( cubo[0] ) 
#cubo[0] = rotacionaFace( cubo[0] ) 
#cubo[0] = rotacionaFace( cubo[0] ) 
#cubo[0] = rotacionaFace( cubo[0] ) 





"""
Testar se:
1) Color instanciada com uma cor continua com aquela cor
2) Se Color errada gera a exception
3) print face[2][1] tem de ser 7, sendo face = 0 
4) face normal e rotacionada. (0 1 2 3 4 5 6 7 8) vira (6 3 0 7 4 1 8 5 2)
5) rotacionar 4 vezes teria de deixar igual no inicio
"""
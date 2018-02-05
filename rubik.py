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
   MAX_FACES = 6
   MAX_LINE = 3
   MAX_COLUMN = 3
   cubo = [[[Color(0, 9*z+3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] for z in range(MAX_FACES)]
   #Definindo quem e vizinho de quem
   VIZINHOS = [[1, 4, 2, 5, 3],
               [3, 0, 2, 5, 4],
               [1, 4, 3, 0, 5],
               [1, 4, 5, 2, 0],
               [0, 1, 2, 5, 1],
               [1, 4, 0, 3, 2], ]
   ACIMA, ABAIXO, DIREITA, ESQUERDA, OPOSTO = range(5)
   
   
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
      
   """ Rotaciona a frente, em 90 graus, sentido horario """
   def rotacionaFrenteHor(self,indice): #antigo rotacionaFace
      face = self.cubo[indice]
      #Tentarei agora rotacionar a tal face
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]][MAX_LINE-1-i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.DIREITA] ][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]   ][2]           [i] #DIREITA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA] ][MAX_LINE-1-i][0] #ABAIXO 
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]  ][0]           [i] #ESQUERDA
      self.cubo = cubo2 #desclonou
      self.cubo[indice] = face2
   
   """ Rotaciona a frente, em 90 graus, sentido anti-horario """
   def rotacionaFrenteAnt(self,indice):
      #Na pratica, eu poderia fazer tres rotacoes no sentido horario. Isso daria no mesmo. Seria o equiavelente a fazer uma subtracao binaria usando apenas a soma.
      self.rotacionaFaceHor(indice)
      self.rotacionaFaceHor(indice)
      self.rotacionaFaceHor(indice)
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido horario """
   def rotacionaEsqHor(self,indice):
      #Na pratica, e equivalente a rotacionar a face esquerda no sentido horario, so que nao
      indice_alt = self.VIZINHOS[indice][self.ESQUERDA] #Pego face que esta na esquerda
      face = self.cubo[indice_alt] #Trabalho apenas com a face esquerda
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      #self.cubo[indice_alt] = face2 #face retorna
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][i][0] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]  ][MAX_LINE-1-i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][i][0] = self.cubo[indice]                              [i]           [0] #ABAIXO 
         cubo2[indice]                              [i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]   ][i]           [0] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]  ][MAX_LINE-1-i][0] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
      
   """ Rotaciona a face esquerda, de cima para baixo, sentido anti-horario """
   def rotacionaEsqAnt(self,indice):
      self.rotacionaEsqHor(indice)
      self.rotacionaEsqHor(indice)
      self.rotacionaEsqHor(indice)
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido horario """
   def rotacionaDirHor(self,indice):
      indice_alt = self.VIZINHOS[indice][self.DIREITA] #Pego face que esta na direita
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][i][2] = self.cubo[indice]                                         [i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][i][2] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]  [MAX_LINE-1-i][0] #ABAIXO 
         cubo2[indice]                              [i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]]             [i][2] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]]   [MAX_LINE-1-i][2] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido anti-horario """
   def rotacionaDirAnt(self,indice):
      self.rotacionaDirHor(indice)
      self.rotacionaDirHor(indice)
      self.rotacionaDirHor(indice)
   
   """ Rotaciona a face de cima, sentido horario """
   def rotacionaCimaHor(self,indice):
      indice_alt = self.VIZINHOS[indice][self.ACIMA] #Pego face que esta acima
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][0][i] = self.cubo[indice]                                         [0][i] #ESQUERDA
         cubo2[self.VIZINHOS[indice][self.DIREITA]] [0][i] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]             [0][i] #DIREITA
         cubo2[indice]                              [0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [0][i] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][0][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [0][i] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
      
   """ Rotaciona a face de cima, sentido anti-horario """
   def rotacionaCimaAnt(self,indice):
      self.rotacionaCimaHor(indice)
      self.rotacionaCimaHor(indice)
      self.rotacionaCimaHor(indice)
   
   """ Rotaciona a face de baixo, sentido horario """
   def rotacionaBaixoHor(self,indice):
      indice_alt = self.VIZINHOS[indice][self.ABAIXO] #Pego face que esta acima
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][2][i] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]             [2][i] #ESQUERDA
         cubo2[self.VIZINHOS[indice][self.DIREITA]] [2][i] = self.cubo[indice]                                         [2][i] #DIREITA
         cubo2[indice]                              [2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [2][i] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][2][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [2][i] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
   
   """ Rotaciona a face de baixo, sentido anti-horario """
   def rotacionaBaixoAnt(self,indice):
      self.rotacionaBaixoHor(indice)
      self.rotacionaBaixoHor(indice)
      self.rotacionaBaixoHor(indice)
   
   """ Rotaciona atras, sentido horario """
   def rotacionaAtrasHor(self,indice):
      indice_alt = self.VIZINHOS[indice][self.OPOSTO] #Pego face que esta oposta
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      from copy import deepcopy
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(MAX_LINE):
         for j in range(MAX_COLUMN):
            face2[i][j] = face[MAX_LINE-1-j][i] #sim, vira apenas isso
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(cubo) #aquela Dolly clonada
      for i in range(MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [i][0] #ABAIXO 
         cubo2[self.VIZINHOS[indice][self.DIREITA] ][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]]  [2][MAX_LINE-1-i] #DIREITA
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]]   [0][MAX_LINE-1-i] #ESQUERDA
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2
   
   """ Rotaciona atras, sentido anti-horario """
   def rotacionaAtrasAnt(self,indice):
      self.rotacionaAtrasHor(indice)
      self.rotacionaAtrasHor(indice)
      self.rotacionaAtrasHor(indice)
   
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
r.rotacionaFrenteHor(0)
#r.rotacionaEsqHor(0)
#r.rotacionaDirHor(0)
#r.rotacionaCimaHor(0)
#r.rotacionaBaixoHor(0)
#r.rotacionaAtrasHor(0)
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
5) rotacionar 4 vezes teria de deixar igual no inicio - para cada tipo de movimento
"""
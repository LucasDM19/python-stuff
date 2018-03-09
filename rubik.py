from copy import deepcopy #Usado bastante

#Classe para as cores do cubo mágico.
#Função clássica é azul, verde, amarelo, branco, vermelho e laranja
#As cores que estão nas faces opostas do cubo são: amarelo/branco, vermelho/laranja e azul/verde.
class Color :
   CoresValidas = list(range(6))
   AZUL, VERDE, AMARELO, BRANCO, VERMELHO, LARANJA = CoresValidas
   def __init__(self, value, id):
      if value in self.CoresValidas :
         self.value = value
         self.id = id
      #TODO: raise invalid value exception
   def getValue(self):
      return self.value
   def __str__(self):
      return str(self.id) #return str( self.value )

class rubikCube:
   MAX_FACES = 6
   MAX_LINE = 3
   MAX_COLUMN = 3
   #Definindo quem e vizinho de quem
   VIZINHOS = [[1, 4, 2, 5, 3],
               [3, 0, 2, 5, 4],
               [1, 4, 3, 0, 5],
               [1, 4, 5, 2, 0],
               [0, 1, 2, 5, 1],
               [1, 4, 0, 3, 2], ]
   ACIMA, ABAIXO, DIREITA, ESQUERDA, OPOSTO = list(range(5))
   
   def __init__(self):
      self.cubo = [[[Color(z, 9*z+3*y+x) for x in range(self.MAX_COLUMN)] for y in range(self.MAX_LINE)] for z in range(self.MAX_FACES)]
   
   """ Determina se o cubo pertence ao grupo G1 (retorna 0) ou nao (retorna 1) """
   def obtemHeuristicaG1(self):
      coords_proibidas = {
         (0, 0, 1) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (0, 1, 0) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (0, 1, 2) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (0, 2, 1) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (1, 0, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (1, 1, 0) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (1, 1, 2) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (1, 2, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (2, 0, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (2, 1, 0) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (2, 1, 2) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (2, 2, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (3, 0, 1) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (3, 1, 0) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (3, 1, 2) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (3, 2, 1) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (4, 0, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (4, 1, 0) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (4, 1, 2) : [(1, 0, 1), (1, 2, 1), (2, 0, 1), (2, 1, 0), (2, 1, 2), (2, 2, 1), (4, 0, 1), (4, 2, 1), (5, 0, 1), (5, 1, 0), (5, 1, 2), (5, 2, 1)],
         (4, 2, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (5, 0, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (5, 1, 0) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (5, 1, 2) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
         (5, 2, 1) : [(0, 0, 1), (0, 1, 0), (0, 1, 2), (0, 2, 1), (1, 1, 0), (1, 1, 2), (3, 0, 1), (3, 1, 0), (3, 1, 2), (3, 2, 1), (4, 1, 0), (4, 1, 2)],
      } # Os lugares aonde as peças não estarão
      
      for z in range(self.MAX_FACES):
         for y in range(self.MAX_LINE):
            for x in range(self.MAX_COLUMN):
               #print( "ID=", traduzIndiceCoordenada( self.cubo[z][y][x].id ), " está em: ", traduzIndiceCoordenada( (9*z+3*y+x) )  ) 
               if traduzIndiceCoordenada( self.cubo[z][y][x].id ) in coords_proibidas:
                  if traduzIndiceCoordenada( (9*z+3*y+x) ) in coords_proibidas[traduzIndiceCoordenada( self.cubo[z][y][x].id )] :
                     #print("Proibidão!!!", coords_proibidas[traduzIndiceCoordenada( self.cubo[z][y][x].id )] )
                     return (9*z+3*y+x)  #Retorno o ID incorreto
      return -1 #Indica que o cubo está no grupo G1
   
   """ Calcula a distancia do cubo ate o ponto inicial """
   def obtemHeuristica(self):
      #return [[[ (self.cubo[z][y][x].id - 9*z+3*y+x) **2 for x in range(self.MAX_COLUMN)] for y in range(self.MAX_LINE)] for z in range(self.MAX_FACES)] 
      heur = 0
      for z in range(self.MAX_FACES):
         for y in range(self.MAX_LINE):
            for x in range(self.MAX_COLUMN):
               heur += ( self.cubo[z][y][x].id - (9*z+3*y+x))**2
               #heur += ( self.cubo[z][y][x].value - (z))**2
      #print (heur*1.0) ** 0.5
      return (heur*1.0) ** 0.5
      
   """ Tentarei Heuristica apenas dos cantos """
   def obtemHeuristicaCanto(self):
      heur = 8
      for z in [0, 3]:
         if self.cubo[z][0][0].id == (9*z+0) : heur -= 1
         if self.cubo[z][0][2].id == (9*z+2) : heur -= 1
         if self.cubo[z][2][0].id == (9*z+6) : heur -= 1
         if self.cubo[z][2][2].id == (9*z+8) : heur -= 1
      #print (heur)
      return heur
   
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
      
   """ Apenas gira uma face """
   def rotacionaFace(self, face):
      #Tentarei agora rotacionar a tal face
      face2 = deepcopy(face) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         for j in range(self.MAX_COLUMN):
            face2[i][j] = face[self.MAX_LINE-1-j][i] #sim, vira apenas isso
      return face2
   
   """ Rotaciona a frente, em 90 graus, sentido horario """
   def rotacionaFrenteHor(self,indice=0): #antigo rotacionaFace
      face = self.cubo[indice]
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]][self.MAX_LINE-1-i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.DIREITA] ][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]   ][2]           [i] #DIREITA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA] ][self.MAX_LINE-1-i][0] #ABAIXO 
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]  ][0]           [i] #ESQUERDA
      self.cubo = cubo2 #desclonou
      self.cubo[indice] = face2
   
   """ Rotaciona a frente, em 90 graus, sentido anti-horario """
   def rotacionaFrenteAnt(self,indice=0):
      #Na pratica, eu poderia fazer tres rotacoes no sentido horario. Isso daria no mesmo. Seria o equiavelente a fazer uma subtracao binaria usando apenas a soma.
      self.rotacionaFrenteHor(indice)
      self.rotacionaFrenteHor(indice)
      self.rotacionaFrenteHor(indice)
      
   """ Rotaciona a frente, em 90 graus, sentido horario, duas vezes """
   def rotacionaFrenteDup(self, indice=0):
      self.rotacionaFrenteHor(indice)
      self.rotacionaFrenteHor(indice)
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido horario """
   def rotacionaEsqHor(self,indice=0):
      #Na pratica, e equivalente a rotacionar a face esquerda no sentido horario, so que nao
      indice_alt = self.VIZINHOS[indice][self.ESQUERDA] #Pego face que esta na esquerda
      face = self.cubo[indice_alt] #Trabalho apenas com a face esquerda
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][i][0] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]  ][self.MAX_LINE-1-i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][i][0] = self.cubo[indice]                              [i]           [0] #ABAIXO 
         cubo2[indice]                              [i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]   ][i]           [0] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]  ][self.MAX_LINE-1-i][0] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
      
   """ Rotaciona a face esquerda, de cima para baixo, sentido anti-horario """
   def rotacionaEsqAnt(self,indice=0):
      self.rotacionaEsqHor(indice)
      self.rotacionaEsqHor(indice)
      self.rotacionaEsqHor(indice)
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido horario, duas vezes """
   def rotacionaEsqDup(self,indice=0):
      self.rotacionaEsqHor(indice)
      self.rotacionaEsqHor(indice)
   
   """ Rotaciona a face direita, de cima para baixo, sentido horario """
   def rotacionaDirHor(self,indice=0):
      indice_alt = self.VIZINHOS[indice][self.DIREITA] #Pego face que esta na direita
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][i][2] = self.cubo[indice]                                         [i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][i][2] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]  [self.MAX_LINE-1-i][0] #ABAIXO 
         cubo2[indice]                              [i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]]             [i][2] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]]   [self.MAX_LINE-1-i][2] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
   
   """ Rotaciona a face direita, de cima para baixo, sentido anti-horario """
   def rotacionaDirAnt(self,indice=0):
      self.rotacionaDirHor(indice)
      self.rotacionaDirHor(indice)
      self.rotacionaDirHor(indice)
      
   """ Rotaciona a face direita, de cima para baixo, sentido horario, duas vezes """
   def rotacionaDirDup(self,indice=0):
      self.rotacionaDirHor(indice)
      self.rotacionaDirHor(indice)
   
   """ Rotaciona a face de cima, sentido horario """
   def rotacionaCimaHor(self,indice=0):
      indice_alt = self.VIZINHOS[indice][self.ACIMA] #Pego face que esta acima
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][0][i] = self.cubo[indice]                                         [0][i] #ESQUERDA
         cubo2[self.VIZINHOS[indice][self.DIREITA]] [0][i] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]             [0][i] #DIREITA
         cubo2[indice]                              [0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [0][i] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][0][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [0][i] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
      
   """ Rotaciona a face de cima, sentido anti-horario """
   def rotacionaCimaAnt(self,indice=0):
      self.rotacionaCimaHor(indice)
      self.rotacionaCimaHor(indice)
      self.rotacionaCimaHor(indice)
   
   """ Rotaciona a face de cima, sentido horario, duas vezes """
   def rotacionaCimaDup(self,indice=0):
      self.rotacionaCimaHor(indice)
      self.rotacionaCimaHor(indice)
   
   """ Rotaciona a face de baixo, sentido horario """
   def rotacionaBaixoHor(self,indice=0):
      indice_alt = self.VIZINHOS[indice][self.ABAIXO] #Pego face que esta acima
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][2][i] = self.cubo[self.VIZINHOS[indice][self.OPOSTO]]             [2][i] #ESQUERDA
         cubo2[self.VIZINHOS[indice][self.DIREITA]] [2][i] = self.cubo[indice]                                         [2][i] #DIREITA
         cubo2[indice]                              [2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [2][i] #atual
         cubo2[self.VIZINHOS[indice][self.OPOSTO]  ][2][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [2][i] #OPOSTO
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2 #face retorna, mas apenas agora
   
   """ Rotaciona a face de baixo, sentido anti-horario """
   def rotacionaBaixoAnt(self,indice=0):
      self.rotacionaBaixoHor(indice)
      self.rotacionaBaixoHor(indice)
      self.rotacionaBaixoHor(indice)
   
   """ Rotaciona a face de baixo, sentido horario, duas vezes """
   def rotacionaBaixoDup(self,indice=0):
      self.rotacionaBaixoHor(indice)
      self.rotacionaBaixoHor(indice)
   
   """ Rotaciona atras, sentido horario """
   def rotacionaAtrasHor(self,indice=0):
      indice_alt = self.VIZINHOS[indice][self.OPOSTO] #Pego face que esta oposta
      face = self.cubo[indice_alt] #Trabalho apenas com a face direita
      face2 = self.rotacionaFace(face) #Rotacionando a face
      
      #Rotacionando os vizinhos
      cubo2 = deepcopy(self.cubo) #aquela Dolly clonada
      for i in range(self.MAX_LINE):
         cubo2[self.VIZINHOS[indice][self.ACIMA]   ][0][i] = self.cubo[self.VIZINHOS[indice][self.DIREITA]]            [i][2] #ACIMA
         cubo2[self.VIZINHOS[indice][self.ABAIXO]  ][2][i] = self.cubo[self.VIZINHOS[indice][self.ESQUERDA]]           [i][0] #ABAIXO 
         cubo2[self.VIZINHOS[indice][self.DIREITA] ][i][2] = self.cubo[self.VIZINHOS[indice][self.ABAIXO]]  [2][self.MAX_LINE-1-i] #DIREITA
         cubo2[self.VIZINHOS[indice][self.ESQUERDA]][i][0] = self.cubo[self.VIZINHOS[indice][self.ACIMA]]   [0][self.MAX_LINE-1-i] #ESQUERDA
      self.cubo = cubo2 #desclonou
      self.cubo[indice_alt] = face2
   
   """ Rotaciona atras, sentido anti-horario """
   def rotacionaAtrasAnt(self,indice=0):
      self.rotacionaAtrasHor(indice)
      self.rotacionaAtrasHor(indice)
      self.rotacionaAtrasHor(indice)
   
   """ Rotaciona atras, sentido horario, duas vezes """
   def rotacionaAtrasDup(self,indice=0):
      self.rotacionaAtrasHor(indice)
      self.rotacionaAtrasHor(indice)

class RubikCubeXplorer:
   cubo = None
   def __init__(self, cubo=None):
      if cubo is None :
         cubo = rubikCube()
      self.cubo = cubo
   
   """ Obtem uma lista de comandos para serem feitos num cubo """
   def efetuaMovimentos(self, lista_movimentos=None, move=None, simulaCubo=False ):
      if lista_movimentos is None:
         lista_movimentos = []
         lista_movimentos.append( move )
      if simulaCubo :
         cubo2 = deepcopy(self.cubo) #Clono o cubo
      else: 
         cubo2 = self.cubo #Mantenho cubo original
      for movimento in lista_movimentos:
         switcher = {
            "F" : cubo2.rotacionaFrenteHor,
            "R" : cubo2.rotacionaDirHor,
            "L" : cubo2.rotacionaEsqHor,
            "U" : cubo2.rotacionaCimaHor,
            "D" : cubo2.rotacionaBaixoHor,
            "B" : cubo2.rotacionaAtrasHor,
            "L2" : cubo2.rotacionaEsqDup,
            "R2" : cubo2.rotacionaDirDup,
            "F2" : cubo2.rotacionaFrenteDup,
            "B2" : cubo2.rotacionaAtrasDup,
            "U2" : cubo2.rotacionaCimaDup,
            "D2" : cubo2.rotacionaBaixoDup,
            "F'" : cubo2.rotacionaFrenteAnt,
            "R'" : cubo2.rotacionaDirAnt,
            "L'" : cubo2.rotacionaEsqAnt,
            "U'" : cubo2.rotacionaCimaAnt,
            "D'" : cubo2.rotacionaBaixoAnt,
            "B'" : cubo2.rotacionaAtrasAnt,
         }
         func = switcher.get(movimento, "Invalido")
         func()  #Executo a funcao
      if simulaCubo :
         return cubo2
      
   """ Obtem um cubo magico e efetua movimentos aleatorios """
   def embaralhaCubo(self, repeticoes=50, switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", } ):
      from random import randrange
      lista_movimentos = []
      #switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }
      for i in range(repeticoes):
         lista_movimentos.append( switcher[ randrange(self.cubo.MAX_FACES) ] )
      self.efetuaMovimentos( lista_movimentos  )

def exploraArvoreAmpla( func_heuristica ):      
   x = RubikCubeXplorer()
   print((x.cubo))
   x.embaralhaCubo(1)
   #x.efetuaMovimentos( ["R","U", "R'", "U", "R", "U", "U", "R'", "U" ] ) #R U R' U R U2 R' U
   operacoes_g0 =   ["F" , "R" , "L" , "U" , "D" , "B" ]
   melhor_mov = ""
   melhor_heu = x.cubo.obtemHeuristica()
   print("Inicio. H=", melhor_heu)
   contador=0
   max_profun = 4  #Ate onde a arvore ira
   for ram in range(1,max_profun+1): #Como uma espiral, varre a arvore, item a item.
      import itertools
      lista_movs = list(itertools.product(operacoes_g0, repeat=ram))  #lista de opcoes possiveis. FFF, FFB, ... , BBD, BBB
      for mov in lista_movs:
         contador +=1
         c2 = x.efetuaMovimentos(mov, None, simulaCubo=True)
         if c2.obtemHeuristica() < melhor_heu:
            melhor_heu = c2.obtemHeuristica()
            melhor_mov = mov
            print("#", contador, "Ram=", ram, "Mov=", melhor_mov, ", H=", melhor_heu)
   x.efetuaMovimentos(melhor_mov, None, simulaCubo=False) #Aplico o melhor movimento
   print((x.cubo))
   
def exploraArvoreProfunda():
   x = RubikCubeXplorer()
   #x.efetuaMovimentos( ["U", ] )
   #print ( "1mov=", x.cubo.obtemHeuristica() )
   print((x.cubo))
   x.embaralhaCubo(10)
   print((x.cubo))
   print ("Heuristica inicial:", x.cubo.obtemHeuristicaCanto() )
   #prof_ramo=25  #Profundidade maxima a ser buscada
   #switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }
   #from random import randrange
   melhor_movs = []
   melhor_heu = x.cubo.obtemHeuristicaCanto()
   melhor_mov_ant = "" #Memoria para nao ficar preso
   cont = 0
   for vezes in range(2000):
      prof_ramo = randrange(42) #Profundidade aleatoria
      #movimento = [switcher[ randrange(x.cubo.MAX_FACES) ] for i in range(prof_ramo)]  #Lista aleatoria candidata
      movimento = obtemMovimentosAleatorios(switcher={0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }, qtd_movs=prof_ramo)
      c2 = x.efetuaMovimentos( movimento, None, simulaCubo=True  )
      if c2.obtemHeuristicaCanto() < melhor_heu:
         melhor_heu = c2.obtemHeuristicaCanto()
         melhor_movs = movimento  #Por enquanto apenas isso
         print ( "Etapa #", cont, ", heur=", c2.obtemHeuristicaCanto(), ", movs=", movimento )
      cont += 1
   x.efetuaMovimentos( melhor_movs, None  ) #A melhor opcao fica sendo a atual
   print((x.cubo))

#Para facilitar. Recebo um numero entre 0 e 53. Retorno (f, l, c), com face entre 0 e 5, linha e coluna entre 0 e 2.
def traduzIndiceCoordenada(indice):
   return ( int(indice/9), int(indice/3) % 3, indice % 3 )

def obtemMovimentosAleatorios(switcher={0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }, qtd_movs=1):
   from random import randrange
   movimento = [switcher[ randrange(len(switcher)) ] for i in range(qtd_movs)]
   return movimento
   
def geraCubosGn(movimentos):
   matriz_total = [[0 for x in range(54)] for y in range(54)] #Contarei as ocorrencias de cada tipo
   for qtd in range(2000):
      xp = RubikCubeXplorer()
      xp.embaralhaCubo(repeticoes=20, switcher=movimentos )
      for z in range(xp.cubo.MAX_FACES):
            for y in range(xp.cubo.MAX_LINE):
               for x in range(xp.cubo.MAX_COLUMN):
                  matriz_total[(9*z+3*y+x)][ xp.cubo.cubo[z][y][x].id ] += 1
      #if( qtd % 100 == 0 ):
      #   print( "#", str(qtd) )

   #Recebe uma coordenada (face, linha, coluna), e informa se eh do tipo canto ('c'), meio('m') ou centro('k') da face.
   def defineCantoMeioCentro(coordenada):
      if( coordenada[1] == int(xp.cubo.MAX_LINE/2) ) and ( coordenada[2] == int(xp.cubo.MAX_COLUMN/2) ) : return "k"  #Coordenadas f,1,1
      if( (coordenada[1]+coordenada[2]) % 2 == 0 ) : return "c"  #Coordenadas f,0,0 f,2,2 f,0,2 e f,2,0
      if( (coordenada[1]+coordenada[2]) % 2 == 1 ) : return "m"  #Coordenadas f,0,1 f,1,0 f,1,2 e f,2,1
      return "?" #Apenas para eviar um erro
        
   #for i in range(54):
      #print(",".join(str(matriz_total[i][j]) for j in range(54)))
   for id in range(54):
      print( "Coor=", traduzIndiceCoordenada(id) )
      for valor in range(54):
         if( (defineCantoMeioCentro(traduzIndiceCoordenada(id)) != "k") 
         and (defineCantoMeioCentro(traduzIndiceCoordenada(id)) == defineCantoMeioCentro(traduzIndiceCoordenada(valor))) ): #Valores especificos
            print("linha=", traduzIndiceCoordenada(valor), "->", matriz_total[id][valor], "(", 100.0*matriz_total[id][valor]/2000, "%)" )
   dic_ids = {} #Dicionario de movimentos a serem buscados
   for id in range(54):
      for valor in range(54):
         if( (defineCantoMeioCentro(traduzIndiceCoordenada(id)) != "k") 
         and (defineCantoMeioCentro(traduzIndiceCoordenada(id)) == defineCantoMeioCentro(traduzIndiceCoordenada(valor)))
         and ( matriz_total[id][valor] == 0) ): #Valores especificos
            #print("ID=", id, ", ", defineCantoMeioCentro(traduzIndiceCoordenada(id)), ",Valor=", valor, ", ", defineCantoMeioCentro(traduzIndiceCoordenada(valor)) )
            if traduzIndiceCoordenada(id) not in dic_ids: dic_ids[traduzIndiceCoordenada(id)] = []
            dic_ids[traduzIndiceCoordenada(id)].append( traduzIndiceCoordenada(valor) )
   # dic_faces = {} #Contabilizar por tipo de coordenada (linha, coluna)
   for id in dic_ids:
      print( "ID=", id, ", len=", len(dic_ids[id]), "->", dic_ids[id] )
      # for p in dic_ids[id]:
         # #if( (p[1], p[2] ) not in dic_faces ): dic_faces[(p[1], p[2] )] = 0
         # if( p[0] not in dic_faces ): dic_faces[p[0]] = []
         # #dic_faces[(p[1], p[2] )] += 1
         # dic_faces[p[0]].append( (p[1], p[2]) )
   
   # for face in dic_faces:
      # print( "Face=", face, ", total=", dic_faces[face] )

""" Função que tenta descobrir quais movimentos são mais efetivos, ao fazer a passagem entre G0 e G1 """
def geraMovimentosG1():
   dic_heur = {} #Heuristicas
   for geracoes in range(100000):  #Aleatoriedade
      x = RubikCubeXplorer()
      x.embaralhaCubo(15)
      heur_ant = x.cubo.obtemHeuristicaG1()
      #print("Ant=", heur_ant)
      for qtd in range(10): #Apenas uma vez?
         #x.embaralhaCubo(15) #Começo do zero, sempre
         movimento = obtemMovimentosAleatorios(switcher={0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", 
                                                         6 : "F2",  7 : "R2", 8 : "L2", 9 : "U2", 10 : "D2", 11 : "B2",
                                                         12 : "F'",  13 : "R'", 14 : "L'", 15 : "U'", 16 : "D'", 17 : "B'", }, qtd_movs=1)
         #print("Movimento=", movimento[0] )
         x.efetuaMovimentos(movimento)
         #print( x.cubo.obtemHeuristicaG1() )
         if (heur_ant < x.cubo.obtemHeuristicaG1()) and (heur_ant != -1) :  #A heuristica tem de melhorar
            #print( "Movimento=", movimento[0], " com heur=", heur_ant ," é bom!")  
            #Caso tenha sucesso, eu registro
            if heur_ant not in dic_heur:
               dic_heur[heur_ant] = {}
            if movimento[0] not in dic_heur[heur_ant] :
               dic_heur[heur_ant][movimento[0]] = 0 
            dic_heur[heur_ant][movimento[0]] += 1 #Contabilizo esse movimento, com a heurística
            heur_ant = x.cubo.obtemHeuristicaG1()  #Atualiza
         #else: print("RUIM!!!!")
   from collections  import OrderedDict
   sorted_dic_heur = {}
   for h in dic_heur:
      sorted_x = OrderedDict(sorted(dic_heur[h].items(), key=lambda x: x[1]))
      #print(sorted_x)
      dic_heur[h] = sorted_x
   for h in dic_heur:
      print ("Heur=", h, "Movs=",dic_heur[h] )
      
def exploraAteG1():
   dic_movimentos={
      1: ("F", "F2", "F'", "U", "U2", "U'", "D", "D2", "D'", "B", "B2", "B'", "R", "R2", "R'"),
      5: ("R", "R2", "R'", "F", "F2", "F'", "L", "L2", "L'"),
      3: ("L", "L2", "L'", "F", "F2", "F'", "U", "U2", "U'", "D", "D2", "D'"),
      10: ("B", "B2", "B'", "U", "U2", "U'"),
      7: ("D", "D2", "D'", "L", "L2", "L'" "R", "R2", "R'"),
      12: ("U", "U2", "U'", "L", "L2", "L'"),
      14: ("R", "R2", "R'", "L", "L2", "L'"),
      23: ("B", "B2", "B'", "R", "R2", "R'",),
      25: ("D", "D2", "D'", "B", "B2", "B'"),
      32: ("L", "L2", "L'", "B", "B2", "B'"),
      }
   x = RubikCubeXplorer()
   x.embaralhaCubo(15)
   cont2 = 0
   while heur != -1 and cont2 < 100 :
      cont2+= 1
      heur_ant = x.cubo.obtemHeuristicaG1()
      print("Melhor mov=", dic_movimentos[heur_ant][0], "heur=", heur_ant)
      y=x.efetuaMovimentos(None, dic_movimentos[heur_ant][0], simulaCubo=True ) 
      heur=y.obtemHeuristicaG1()
      print("Heur=",heur )
      cont=0
      while heur_ant == heur and cont < 16 :
         cont += 1
         print("Plano#", cont, dic_movimentos[heur_ant][cont] )
         y=x.efetuaMovimentos(None, dic_movimentos[heur_ant][cont], simulaCubo=True ) 
         heur=y.obtemHeuristicaG1()
         print("Heur=", heur )
      print("Melhor mov=", dic_movimentos[heur_ant][cont], "heur=", heur)
      x.efetuaMovimentos(None, dic_movimentos[heur_ant][cont], simulaCubo=True ) #Realizando o movimento
#x = RubikCubeXplorer()
#print (x.cubo)
#exploraArvoreAmpla( rubikCube().obtemHeuristica )
#exploraArvoreProfunda()
#geraCubosGn(movimentos={0 : "F",   1 : "R",  2 : "L",  3 : "U",  4 : "D",  5 : "B", }) #Movimentos para G0
#geraCubosGn(movimentos={0 : "F",   1 : "R",  2 : "L",  3 : "U2", 4 : "D2", 5 : "B", }) #Movimentos para G1
#geraCubosGn(movimentos={0 : "F2",  1 : "R",  2 : "L",  3 : "U2", 4 : "D2", 5 : "B2", }) #Movimentos para G2
#geraCubosGn(movimentos={0 : "F2",  1 : "R2", 2 : "L2", 3 : "U2", 4 : "D2", 5 : "B2", }) #Movimentos para G3
#x.cubo.obtemHeuristicaCanto()
#geraMovimentosG1()
exploraAteG1()
#x.efetuaMovimentos(None, "L")
#x.embaralhaCubo(10)
#x.cubo.obtemHeuristicaCanto()

"""
Testar se:
1) Color instanciada com uma cor continua com aquela cor
2) Se Color errada gera a exception
3) print face[2][1] tem de ser 7, sendo face = 0 
4) face normal e rotacionada. (0 1 2 3 4 5 6 7 8) vira (6 3 0 7 4 1 8 5 2)
5) rotacionar 4 vezes teria de deixar igual no inicio - para cada tipo de movimento
"""
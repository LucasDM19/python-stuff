from copy import deepcopy #Usado bastante

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
      return str(self.value) #return str( self.id )

class rubikCube:
   MAX_FACES = 6
   MAX_LINE = 3
   MAX_COLUMN = 3
   cubo = [[[Color(z, 9*z+3*y+x) for x in range(MAX_COLUMN)] for y in range(MAX_LINE)] for z in range(MAX_FACES)]
   #Definindo quem e vizinho de quem
   VIZINHOS = [[1, 4, 2, 5, 3],
               [3, 0, 2, 5, 4],
               [1, 4, 3, 0, 5],
               [1, 4, 5, 2, 0],
               [0, 1, 2, 5, 1],
               [1, 4, 0, 3, 2], ]
   ACIMA, ABAIXO, DIREITA, ESQUERDA, OPOSTO = range(5)
   
   """ Calcula a distancia do cubo ate o ponto inicial """
   def obtemHeuristica(self):
      #return [[[ (self.cubo[z][y][x].id - 9*z+3*y+x) **2 for x in range(self.MAX_COLUMN)] for y in range(self.MAX_LINE)] for z in range(self.MAX_FACES)] 
      heur = 0
      for z in range(self.MAX_FACES):
         for y in range(self.MAX_LINE):
            for x in range(self.MAX_COLUMN):
               #print "id=", self.cubo[z][y][x].id, ", clc=", 9*z+3*y+x, ", dif=", ( self.cubo[z][y][x].id - (9*z+3*y+x)), " # z=", str(z), ", y=", str(y), ", x=", str(x)
               #if self.cubo[z][y][x].id != 9*z+3*y+x :
               #   cont += 1
               heur += ( self.cubo[z][y][x].id - (9*z+3*y+x))**2
      #print (heur*1.0) ** 0.5
      return (heur*1.0) ** 0.5
   
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
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido horario """
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
   
   """ Rotaciona a face esquerda, de cima para baixo, sentido anti-horario """
   def rotacionaDirAnt(self,indice=0):
      self.rotacionaDirHor(indice)
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
   

class RubikCubeXplorer:
   cubo = None
   def __init__(self, cubo=None):
      if cubo is None :
         cubo = rubikCube()
      self.cubo = cubo
   
   """ Obtem uma lista de comandos para serem feitos num cubo """
   def efetuaMovimentos(self, lista_movimentos=None, move=None ):
      if lista_movimentos is None:
         lista_movimentos = []
         lista_movimentos.append( move )
      for movimento in lista_movimentos:
         switcher = {
            "F" : self.cubo.rotacionaFrenteHor,
            "R" : self.cubo.rotacionaDirHor,
            "L" : self.cubo.rotacionaEsqHor,
            "U" : self.cubo.rotacionaCimaHor,
            "D" : self.cubo.rotacionaBaixoHor,
            "B" : self.cubo.rotacionaAtrasHor,
            "F'" : self.cubo.rotacionaFrenteAnt,
            "R'" : self.cubo.rotacionaDirAnt,
            "L'" : self.cubo.rotacionaEsqAnt,
            "U'" : self.cubo.rotacionaCimaAnt,
            "D'" : self.cubo.rotacionaBaixoAnt,
            "B'" : self.cubo.rotacionaAtrasAnt,
         }
         func = switcher.get(movimento, "Invalido")
         func()  #Executo a funcao
      
   """ Obtem um cubo magico e efetua movimentos aleatorios """
   def embaralhaCubo(self, repeticoes=50):
      from random import randrange
      lista_movimentos = []
      switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }
      for i in range(repeticoes):
         lista_movimentos.append( switcher[ randrange(self.cubo.MAX_FACES) ] )
      self.efetuaMovimentos( lista_movimentos  )

def exploraArvoreAmpla():      
   x = RubikCubeXplorer()
   x.embaralhaCubo(1000)
   #x.efetuaMovimentos( ["R","U", "R'", "U", "R", "U", "U", "R'", "U" ] ) #R U R' U R U2 R' U
   ida =   ["F" , "R" , "L" , "U" , "D" , "B" , "F'", "R'", "L'", "U'", "D'", "B'",] 
   volta = ["F'", "R'", "L'", "U'", "D'", "B'", "F" , "R" , "L" , "U" , "D" , "B" ,]
   melhor_mov = ""
   melhor_heu = 10000000
   melhor_mov_ant = "" #Memoria para nao ficar preso
   for vezes in range(42):
      for m in range(len(ida)) :  #Avaliando os movimentos possiveis
         x.efetuaMovimentos( None, ida[m] )
         #print ida[m],", ", x.cubo.obtemHeuristica()
         if x.cubo.obtemHeuristica() < melhor_heu:
            melhor_heu = x.cubo.obtemHeuristica()
            melhor_mov = ida[m]
         x.efetuaMovimentos( None, volta[m] )
         movs = []
      if melhor_mov == melhor_mov_ant :
         #print "Estagnado num pico local. Insanity!"
         import random
         melhor_mov = random.choice(ida) #Quando nao se sabe aonde ir, qualquer caminho esta bom
         melhor_heu = 10000000 #Esquecendo do passado
      print "#", vezes, "Mov=", melhor_mov, ", H=", melhor_heu
      melhor_mov_ant = melhor_mov #Para se lembrar
      x.efetuaMovimentos( None, melhor_mov )
   print x.cubo
   
#x = RubikCubeXplorer()
#print x.cubo.obtemHeuristica()
exploraArvoreAmpla()
"""
Testar se:
1) Color instanciada com uma cor continua com aquela cor
2) Se Color errada gera a exception
3) print face[2][1] tem de ser 7, sendo face = 0 
4) face normal e rotacionada. (0 1 2 3 4 5 6 7 8) vira (6 3 0 7 4 1 8 5 2)
5) rotacionar 4 vezes teria de deixar igual no inicio - para cada tipo de movimento
"""
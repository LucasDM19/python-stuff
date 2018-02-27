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
   def embaralhaCubo(self, repeticoes=50):
      from random import randrange
      lista_movimentos = []
      switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }
      for i in range(repeticoes):
         lista_movimentos.append( switcher[ randrange(self.cubo.MAX_FACES) ] )
      self.efetuaMovimentos( lista_movimentos  )

def exploraArvoreAmpla():      
   x = RubikCubeXplorer()
   x.embaralhaCubo(4)
   #x.efetuaMovimentos( ["R","U", "R'", "U", "R", "U", "U", "R'", "U" ] ) #R U R' U R U2 R' U
   operacoes_g0 =   ["F" , "R" , "L" , "U" , "D" , "B" ]
   melhor_mov = ""
   melhor_heu = x.cubo.obtemHeuristica()
   print("Inicio. H=", melhor_heu)
   contador=0
   max_profun = 6  #Ate onde a arvore ira
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
   switcher = {0 : "F",  1 : "R", 2 : "L", 3 : "U", 4 : "D", 5 : "B", }
   from random import randrange
   melhor_movs = []
   melhor_heu = x.cubo.obtemHeuristicaCanto()
   melhor_mov_ant = "" #Memoria para nao ficar preso
   cont = 0
   for vezes in range(2000):
      prof_ramo = randrange(42) #Profundidade aleatoria
      movimento = [switcher[ randrange(x.cubo.MAX_FACES) ] for i in range(prof_ramo)]  #Lista aleatoria candidata
      c2 = x.efetuaMovimentos( movimento, None, simulaCubo=True  )
      if c2.obtemHeuristicaCanto() < melhor_heu:
         melhor_heu = c2.obtemHeuristicaCanto()
         melhor_movs = movimento  #Por enquanto apenas isso
         print ( "Etapa #", cont, ", heur=", c2.obtemHeuristicaCanto(), ", movs=", movimento )
      cont += 1
   x.efetuaMovimentos( melhor_movs, None  ) #A melhor opcao fica sendo a atual
   print((x.cubo))
   
#x = RubikCubeXplorer()
#print x.cubo.obtemHeuristica()
exploraArvoreAmpla()
#exploraArvoreProfunda()
#x = RubikCubeXplorer()
#x.cubo.obtemHeuristicaCanto()
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
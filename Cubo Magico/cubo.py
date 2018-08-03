"""
   Representando um cubo.
   Ele tem 6 faces.
   Ele tera as 6 operacoes padrao, mais as 6 operacoes inversas.
   Talvez tenha a opcao de suportar a operacao de "virar" (mudar a referencia das faces.
"""
class Cube:
   faceF, faceB, faceD, faceU, faceL, faceR = None, None, None, None, None, None
   def __init__(self):
      self.initializeFaces() #Defino as cores de cada face
      self.defineNeighbourhood() #Defino aonde esta cada peca central
      self.inicializeAllColors() #Defino As cores de cada linha
      self.initializeAllPieces() #Com base nas cores proprias e dos vizinhos, defino as pecas
      
   """ Por enquanto, inicializo um cubo ok """
   def initializeFaces(self):
      self.faceF = Face( VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE ) #Face Front
      self.faceB = Face( AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL ) #Face Back
      self.faceD = Face( LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA ) #Face Down
      self.faceU = Face( VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO ) #Face Up
      self.faceL = Face( AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO ) #Face Left
      self.faceR = Face( BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO ) #Face Right
      
   def defineNeighbourhood(self):
      self.faceF.setNeighbours( self.faceU, self.faceR, self.faceD, self.faceL, self.faceB ) #sentido horario, comecando por cima
      self.faceB.setNeighbours( self.faceU, self.faceL, self.faceD, self.faceR, self.faceF ) #girei o cubo na minha mao, 180 graus, sentido horario
      self.faceD.setNeighbours( self.faceF, self.faceR, self.faceB, self.faceL, self.faceU)
      self.faceU.setNeighbours( self.faceB, self.faceR, self.faceF, self.faceL, self.faceD)
      self.faceL.setNeighbours( self.faceU, self.faceF, self.faceD, self.faceB, self.faceR )
      self.faceR.setNeighbours( self.faceU, self.faceB, self.faceD, self.faceF, self.faceL )
      
   def inicializeAllColors(self):
      self.faceF.initializeColors()
      self.faceB.initializeColors()
      self.faceD.initializeColors()
      self.faceU.initializeColors()
      self.faceL.initializeColors()
      self.faceR.initializeColors()
   
   def initializeAllPieces(self):
      self.faceF.initializePieces2()
      self.faceB.initializePieces2()
      self.faceD.initializePieces2()
      self.faceU.initializePieces2()
      self.faceL.initializePieces2()
      self.faceR.initializePieces2()
      
   """ Rotaciona a frente, em 90 graus, sentido horario """
   def makeMoveF(self):
      prettyFace = self.faceF #Face temporaria
      prettyFace.rotate()     #A face sera girada, 90 graus em sentido horario
      print self.faceU.line3, self.faceL.line2, self.faceD.line1, self.faceR.line4
      print self.faceU.line3.color1, self.faceU.line3.color2, self.faceU.line3.color3
      l = self.faceU.getLine3() #Salvo linha
      self.faceU.line3 = self.faceL.getLine2()
      self.faceL.line2 = self.faceD.getLine1()
      self.faceD.line1 = self.faceR.getLine4()
      self.faceR.line4 = l
      print self.faceU.line3, self.faceL.line2, self.faceD.line1, self.faceR.line4
      print self.faceU.line3.color1, self.faceU.line3.color2, self.faceU.line3.color3
      self.faceF = prettyFace

   """ Rotaciona atras, em 90 graus, sentido horario """
   def makeMoveB(self):
      self.faceB.setRotation() #A face sera girada, 90 graus em sentido horario
      
   """ Rotaciona abaixo, em 90 graus, sentido horario """
   def makeMoveD(self):
      self.faceD.setRotation() #A face sera girada, 90 graus em sentido horario
      
   """ Rotaciona acima, em 90 graus, sentido horario """
   def makeMoveU(self):
      self.faceU.setRotation() #A face sera girada, 90 graus em sentido horario

   """ Rotaciona a esquerda, em 90 graus, sentido horario """
   def makeMoveL(self):
      self.faceL.setRotation() #A face sera girada, 90 graus em sentido horario

   """ Rotaciona a direita, em 90 graus, sentido horario """
   def makeMoveR(self):
      self.faceR.setRotation() #A face sera girada, 90 graus em sentido horario
      
   def __str__(self):
      BLANK_LINE = "      "
      FILLER = "-----------------------------" 
      line1  = BLANK_LINE + str( self.faceU.color1 ) + "|" + str( self.faceU.color2 ) + "|" + str( self.faceU.color3 ) + "\n"
      line2  = BLANK_LINE + str( self.faceU.color4 ) + "|" + str( self.faceU.color5 ) + "|" + str( self.faceU.color6 ) + "\n"
      line3  = BLANK_LINE + str( self.faceU.color7 ) + "|" + str( self.faceU.color8 ) + "|" + str( self.faceU.color9 ) + "\n"
      line4  = FILLER + "\n"
      line5  = str( self.faceL.color1 ) + "|" + str( self.faceL.color2 ) + "|" + str( self.faceL.color3 ) + "|" + str( self.faceF.color1 ) + "|" + str( self.faceF.color2 ) + "|" + str( self.faceF.color3 ) + "|" + str( self.faceR.color1 ) + "|" + str( self.faceR.color2 ) + "|" + str( self.faceR.color3 ) + "|" + str( self.faceB.color1 ) + "|" + str( self.faceB.color2 ) + "|" + str( self.faceB.color3 ) +"\n"
      line6  = str( self.faceL.color4 ) + "|" + str( self.faceL.color5 ) + "|" + str( self.faceL.color6 ) + "|" + str( self.faceF.color4 ) + "|" + str( self.faceF.color5 ) + "|" + str( self.faceF.color6 ) + "|" + str( self.faceR.color4 ) + "|" + str( self.faceR.color5 ) + "|" + str( self.faceR.color6 ) + "|" + str( self.faceB.color4 ) + "|" + str( self.faceB.color5 ) + "|" + str( self.faceB.color6 ) +"\n"
      line7  = str( self.faceL.color7 ) + "|" + str( self.faceL.color8 ) + "|" + str( self.faceL.color9 ) + "|" + str( self.faceF.color7 ) + "|" + str( self.faceF.color8 ) + "|" + str( self.faceF.color9 ) + "|" + str( self.faceR.color7 ) + "|" + str( self.faceR.color8 ) + "|" + str( self.faceR.color9 ) + "|" + str( self.faceB.color7 ) + "|" + str( self.faceB.color8 ) + "|" + str( self.faceB.color9 ) +"\n"
      line8  = FILLER + "\n"
      line9  = BLANK_LINE + str( self.faceD.color1 ) + "|" + str( self.faceD.color2 ) + "|" + str( self.faceD.color3 ) + "\n"
      line10 = BLANK_LINE + str( self.faceD.color4 ) + "|" + str( self.faceD.color5 ) + "|" + str( self.faceD.color6 ) + "\n"
      line11 = BLANK_LINE + str( self.faceD.color7 ) + "|" + str( self.faceD.color8 ) + "|" + str( self.faceD.color9 ) + "\n"      
      return line1+line2+line3+line4+line5+line6+line7+line8+line9+line10+line11
      
   """ Metodo que eh chamado quando se da um print no objeto Cubo. Simplesmente delego para cada face se representar """
   def toString(self):
      line1 = str(self.faceU) 
      line2 = " " + "\n"
      line3 = str(self.faceL)
      line4 = str(self.faceF)
      line5 = str(self.faceR)
      line6 = str(self.faceB)
      line7 = " " + "\n"
      line8 = str(self.faceD)
      return line1+line2+line3+line4+line5+line6+line7+line8
            
"""
   Representando cada face do cubo.
   Ela tem de ter suporte para operacoes, para modificar seu valor.
   Ao ser criada, cada face pode ser associada com um vizinho.
   Assim, cada operacao nessa face, ira convocar as outras mudancas nas vizinhas, se for o caso.
   Cada operacao afeta o valor das 4 vizinhas. Cada operacao OperacaoX ira "acordar" a vizinha, mandando o seu valor atual. Essa vizinha, recebe o valor novo da linha, e manda a linha dela para a outra, acordando-a. 
   O ciclo acima acaba quando o valor recebido eh igual ao atual.
   Cada face contem 9 pecas, sendo que 4 sao cantos, 4 sao lados, e uma eh a central.
   Para facilitar movimentacoes, cada face tera tambem quatro linhas, numeradas de cima para baixo, em sentido horario. Em cada operacao simples, apenas uma delas sofrera mudanca.
"""
class Face:
   color1, color2, color3, color4, crolo5, color6, color7, color8, color9 = None, None, None, None, None, None, None, None, None
   piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9 = None, None, None, None, None, None, None, None, None
   line1, line2, line3, line4 = None, None, None, None
   NeighbourB, NeighbourD, NeighbourU, NeighbourL, NeighbourR = None, None, None, None, None
   
   def __init__(self, c1, c2, c3, c4, c5, c6, c7, c8, c9):
      self.color1, self.color2, self.color3, self.color4, self.color5, self.color6, self.color7, self.color8, self.color9 = c1, c2, c3, c4, c5, c6, c7, c8, c9
   
   def initializeColors(self):
      self.line1 = Line( self.color1, self.color2, self.color3 )
      self.line2 = Line( self.color3, self.color6, self.color9 )
      self.line3 = Line( self.color7, self.color8, self.color9 )
      self.line4 = Line( self.color1, self.color4, self.color7 )
   
   """ Criando as pecas validas, com base nas minhas cores e dos vizinhos, e as organizando em linhas horizontais e verticais """
   def initializePieces2(self):
      self.piece1 = Piece( self.color1, self.NeighbourU.getLine3().getColor1(), self.NeighbourL.getLine1().getColor3() )
      self.piece2 = Piece( self.color2, self.NeighbourU.getLine3().getColor2() )
      self.piece3 = Piece( self.color3, self.NeighbourU.getLine3().getColor3(), self.NeighbourR.getLine1().getColor1() )
      self.piece4 = Piece( self.color4, self.NeighbourL.getLine2().getColor2() )
      self.piece5 = Piece( self.color5 )
      self.piece6 = Piece( self.color6, self.NeighbourR.getLine4().getColor2() )
      self.piece7 = Piece( self.color7, self.NeighbourL.getLine3().getColor3(), self.NeighbourD.getLine1().getColor1() )
      self.piece8 = Piece( self.color8, self.NeighbourD.getLine1().getColor2() )
      self.piece9 = Piece( self.color9, self.NeighbourR.getLine3().getColor1(), self.NeighbourD.getLine1().getColor3() )
      self.line1.setPieces( self.piece1, self.piece2, self.piece3 )
      self.line2.setPieces( self.piece3, self.piece6, self.piece9 )
      self.line3.setPieces( self.piece7, self.piece8, self.piece9 )
      self.line4.setPieces( self.piece1, self.piece4, self.piece7 )
      
   def getLine1(self):
      return self.line1
      
   def getLine2(self):
      return self.line2
      
   def getLine3(self):
      return self.line3
      
   def getLine4(self):
      return self.line4
         
   """ Identificando aonde as faces estao, com referencia a essa face. Padrao eh, Up, Right, Down, Left, Back. Ou seja, essa propria face estaria como Front.  """
   def setNeighbours( self, f1, f2, f3, f4, f5 ):
      self.NeighbourU, self.NeighbourR, self.NeighbourD, self.NeighbourL, self.NeighbourB = f1, f2, f3, f4, f5
      
   def initializePieces():
      self.initializePieces() #So depois que da para criar pecas, com base nas cores

   """ Quando rotaciono a face, em sentido horario. As outras faces nao importam aqui """
   def rotate(self):
      #self.NeighbourU.updateLineD( self.NeighbourL.getLine2() ) #Linha de um vai para o outro
      l = self.line1 #Salvo
      self.line1 = self.line4
      self.line4 = self.line3
      self.line3 = self.line2
      self.line2 = l
      
   """ Quando rotaciono a face, em sentido ant-horario """
   def setRotationInv(self):
      self.NeighbourU.updateLineDInv( self.NeighbourR.getLine4() ) #Linha de um vai para o outro
                  
   """ Quando rotaciono Down, sentido horario, em relacao a face em questao """
   def updateLineD( self, newLine ):
      print str(self.line3) + "-" + str(newLine)
      if self.line3 == newLine : #Nao faco nada, pois nao ha o que ser feito
         return
      lineN = self.line3 #Salvo ex-linha
      self.line3 = newLine #Atualizo linha
      self.NeighbourR.updateLineD( lineN ) #Mando linha linha para o vizinho
      
   """ Quando rotaciono Down, sentido ant-horario, em relacao a face em questao """
   def updateLineDInv( self, newLine ):      
      if self.line3 == newLine : #Nao faco nada, pois nao ha o que ser feito
         return
      lineN = self.line3 #Salvo ex-linha
      self.linha3 = newLine #Atualizo linha
      self.NeighbourL.updateLineD( lineN ) #Mando linha linha para o vizinho
   
   """ Metodo que e chamado quando se da um print em uma face """
   def __str__(self):
      STATIC_LINE = "-------" + "\n" 
      line1 = STATIC_LINE + "|" + str(self.color1) + "|" + str(self.color2) + "|" + str(self.color3) + "|" + "\n" 
      line2 = STATIC_LINE + "|" + str(self.color4) + "|" + str(self.color5) + "|" + str(self.color6) + "|" + "\n" 
      line3 = STATIC_LINE + "|" + str(self.color7) + "|" + str(self.color8) + "|" + str(self.color9) + "|" + "\n" + STATIC_LINE
      return line1+line2+line3
"""
   Representando uma linha.
   Cada linha tera 6 propriedades:
   -3 objetos Peca validos (qualquer um ds 8 cantos + 12 pecas laterais, total de 20 tipos de pecas)
   -3 cores validas (verde, laranja,amarelo, branco, azul)
"""
class Line:
   piece1, piece2, piece3 = None, None, None
   color1, color2, color3 = None, None, None
   
   def __init__(self, c1, c2, c3, p1=None, p2=None, p3=None):
      self.piece1, self.piece2, self.piece3 = p1, p2, p3
      self.color1, self.color2, self.color3 = c1, c2, c3
      
   def setPieces( self, p1, p2, p3 ):
      self.piece1, self.piece2, self.piece3 = p1, p2, p3
      
   def getColor1(self):
      return self.color1
      
   def getColor2(self):
      return self.color2
      
   def getColor3(self):
      return self.color3
      
   def __str__(self):
      return str(self.color1) + "|" + str(self.color2) + "|" + str(self.color3)
      
"""
   Representando uma peca. Uma notacao que represente numericamente cada uma ajudaria. 
   Tem 6 pecas centrais; Cada peca central eh identificada por um numero, que seria a cor. Verde=0, Laranja=1, Amarelo=2, Vermelho=3, Branco=4, Azul=5
                                                                                           Verde=2, Laranja=3, Amarelo=5, Vermelho=7, Branco=11, Azul=13
   Tem 8 cantos; Cada canto eh uma conjuncao de 3 cores.
      -Verde, Amarelo, Vermelho = (0, 2, 3) = 2*5*7=70
      -Verde, Vermelho, Branco  = (0, 3, 4) = 2*7*11=154
      -Verde, Laranja, Branco   = (0, 1, 4) = 2*3*11=66
      -Verde, Laranja, Amarelo  = (0, 1, 2) = 2*3*5=30
      -Laranja, Amarelo, Azul   = (1, 2, 5) = 3*5*13=195
      -Laranja, Branco, Azul    = (1, 4, 5) = 3*11*13=429
      -Vermelho, Branco, Azul   = (3, 4, 5) = 7*11*13=1001
      -Amarelo, Vermelho, Azul  = (2, 3, 5) = 5*7*13=455
   Tem 12 pecas laterais; Cada lado eh uma conjuncao de 2 cores. 
      -Verde, Laranja    = (0, 1) = 2*3=6
      -Verde, Amarelo    = (0, 2) = 2*5=10
      -Verde, Vermelho   = (0, 3) = 2*7=14
      -Verde, Branco     = (0, 4) = 2*11=22
      -Laranja, Azul     = (1, 5) = 3*13=39
      -Amarelo, Azul     = (2, 5) = 5*13=65
      -Vermelho, Azul    = (3, 5) = 7*13=91
      -Branco, Azul      = (4, 5) = 11*13=143
      -Laranja, Amarelo  = (1, 2) = 3*5=15
      -Laranja, Branco   = (1, 4) = 3*11=33
      -Amarelo, Vermelho = (2, 3) = 5*7=35
      -Vermelho, Branco  = (3, 4) = 7*11=77
"""

VERDE, LARANJA, AMARELO, VERMELHO, BRANCO, AZUL = [2, 3, 5, 7, 11, 13] #Devem ser numeros primos - uso multiplicacao como hash
LISTA_CORES = [VERDE, LARANJA, AMARELO, VERMELHO, BRANCO, AZUL]
PECAS_VALIDAS = [VERDE, LARANJA, AMARELO, VERMELHO, BRANCO, AZUL, #Pecas centrais
                 VERDE*AMARELO*VERMELHO, VERDE*VERMELHO*BRANCO, VERDE*LARANJA*BRANCO, VERDE*LARANJA*AMARELO, LARANJA*AMARELO*AZUL, LARANJA*BRANCO*AZUL, VERMELHO*BRANCO*AZUL, AMARELO*VERMELHO*AZUL,
                 VERDE*LARANJA, VERDE*AMARELO, VERDE*VERMELHO, VERDE*BRANCO, LARANJA*AZUL, AMARELO*AZUL, VERMELHO*AZUL, BRANCO*AZUL, LARANJA*AMARELO, LARANJA*BRANCO, AMARELO*VERMELHO, VERMELHO*BRANCO, ]
#print PECAS_VALIDAS
class Piece:
   pieceID = -1
   #Inicializa uma peca simples, de quina ou de lado. Tem de passar de 1 a 3 parametros.
   def __init__(self, color1, color2=1, color3=1):
      p = color1*color2*color3
      if p not in PECAS_VALIDAS:
         raise Exception("Configuracao invalida!" + color1, color2, color3)
      self.pieceID = p
      
   #Com base no hash armazenado, retorna as cores
   def getColors(self):
      lst = []
      tmp = self.pieceID
      for c in LISTA_CORES:
         if tmp % c == 0:
            lst.append(c)
            tmp = tmp / c
      return lst
            

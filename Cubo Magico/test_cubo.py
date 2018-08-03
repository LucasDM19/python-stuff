from cubo import *

import unittest
class TestCube(unittest.TestCase):
   def testPiecesOfCubeSimple(self):
      #Testando tipos de pecas
      self.assertEqual( Piece( VERDE ).pieceID, 2 ) #Testando peca simples
      self.assertEqual( Piece( VERDE, LARANJA ).pieceID, 6 ) #Testando peca de lado
      self.assertEqual( Piece( VERDE, LARANJA, AMARELO ).pieceID, 30 ) #Testando peca de quina
      #Testando pecas invalidas
      self.assertRaises(Exception, Piece, -1)  
      self.assertRaises(Exception, Piece, VERDE, AZUL) 
      self.assertRaises(Exception, Piece, VERDE, AMARELO, AZUL)
      #Testando funcao contraria
      self.assertEqual( [VERDE], Piece( VERDE ).getColors() )
      self.assertEqual( [VERDE, LARANJA], Piece( VERDE, LARANJA ).getColors() )
      self.assertEqual( [VERDE, LARANJA, AMARELO], Piece( VERDE, LARANJA, AMARELO ).getColors() )
      
   def testFacesSimple(self):
      faceF = Face( VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE, VERDE ) #Face Front
      faceB = Face( AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL, AZUL ) #Face Back
      faceD = Face( LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA, LARANJA ) #Face Down
      faceU = Face( VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO, VERMELHO ) #Face Up
      faceL = Face( AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO, AMARELO ) #Face Left
      faceR = Face( BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO, BRANCO ) #Face Right
      faceF.setNeighbours( faceU, faceR, faceD, faceL, faceB )
      self.assertEqual( faceF.NeighbourU, faceU )
      self.assertEqual( faceF.NeighbourR, faceR )
      self.assertEqual( faceF.NeighbourD, faceD )
      self.assertEqual( faceF.NeighbourL, faceL )
      self.assertEqual( faceF.NeighbourB, faceB )
      
   def testCubeSimple(self):
      c = Cube()
      print(c) #Antes
      c.makeMoveF() #Giro a frente
      print(c) #Depois
   
def main():
    unittest.main()

if __name__ == '__main__':
   main()
    
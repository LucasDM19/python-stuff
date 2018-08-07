#coding=utf-8
"""
 Experimento do dia 23/12/2015
 A pedido do Ronaldo, 'For science!', executarei uma vez o código abaixo, 
 que tem como objetivo gerar 10000 números binários, entre 0 e 1. 
 Deixarei a entrada salva, durante alguns meses.
"""
import random
print [random.randint(0, 1) for i in range(10000)]

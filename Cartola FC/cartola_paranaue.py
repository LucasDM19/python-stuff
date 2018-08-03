# -*- coding: utf-8 -*-

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5

"""
Eu estava pensando em analisar, e ver se tem bons jogadores, que sejam regulares. 
Escolher os jogadores que tragam mais retorno, com menos dinheiro. 
Eu usaria o histórico do jogador para tirar o desvio padrão. 
Aí tiraria a média/(desvio*custo).
Os melhores nesse índice poderiam ser escalados, em teoria. 
"""

import urllib.request, urllib.error, urllib.parse
import json

#Montando um indice de jogadores, e pontuacao a cada rodada
lista_jsons =  {"R05" : 'http://aposte.me/t/cartola__5.json',
				"R06" : 'http://aposte.me/t/cartola__6.json',
				"R07" : 'http://aposte.me/t/cartola__7.json',
				"R08" : 'http://aposte.me/t/cartola__8.json',
				"R09" : 'http://aposte.me/t/cartola__9.json',
				#"R10" : 'http://aposte.me/t/cartola__10.json',
				#"R11" : 'http://aposte.me/t/cartola__11.json',
				#"R12" : 'http://aposte.me/t/cartola__12.json',
				#"R13" : 'http://aposte.me/t/cartola__13.json',
				#"R14" : 'http://aposte.me/t/cartola__14.json',
			   }
dados = {} #lista com totais de pontuacao indexados pelo idx do jogador
for rodada in list(lista_jsons.keys()):
	response = urllib.request.urlopen(lista_jsons[rodada]) #response = urllib2.urlopen('http://aposte.me/t/cartola__5.json')
	data = json.load(response)   
	
	for i in range(len(data["jogadores"])):
		novo_registro = { "pontos": data["jogadores"][i]["pontos"] ,
		} #Lay out da maneira que eu quero
		#novo_registro =  data["jogadores"][i]["pontos"] 
		if str(data["jogadores"][i]["id"]) + data["jogadores"][i]["apelido"] not in dados:
			#dados[str(data["jogadores"][i]["id"]) + data["jogadores"][i]["apelido"]] = {rodada : novo_registro }
			dados[str(data["jogadores"][i]["id"]) + data["jogadores"][i]["apelido"]] = [novo_registro,]
		else:
			dados[str(data["jogadores"][i]["id"]) + data["jogadores"][i]["apelido"]].append( novo_registro)
#print dados["68911Diego Souza"] , pstdev( dados["68911Diego Souza"]  )
	
#Uso de 5 a 9 para calcular DP e media. 10 a 14 sao palpites.
#Para rodada 10, inicialmente
for jogador in list(dados.keys()):
	if len(dados[jogador]) > 2 and pstdev( dados[jogador] ) != 0 :
		print("jogador=", jogador, "DP=", pstdev( dados[jogador] ), "Media=", mean( dados[jogador] ), "Md/dp", mean( dados[jogador] )/pstdev( dados[jogador] ))
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
O metodo define as restricoes, resolve o problema.
Pode mostrar na tela o resultado obtido.
Precisa do esquema tatico passado como parametro.
Retorna o total da media estimada.
"""
def modelaCalcula(Esquema_Tatico,silencio=True):
	if not silencio : print("Esquema: ", Esquema_Tatico)
	prob = LpProblem("Melhor escalacao Cartola FC", LpMaximize)

	#Coloca a primeira condicão, que será o objetivo. Queremos a maior média conjunta
	prob += lpSum([medias[i]*jogadores_vars[i] for i in Jogadores]),'Soma das Medias'

	#Abaixo vamos colocando as restrições
	prob += lpSum([precos[i]*jogadores_vars[i] for i in Jogadores]) <= Preco_Maximo, 'Preco Maximo do Time'

	prob += lpSum([posGOL[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['GOL'], 'Num Goleiros'
	prob += lpSum([posZAG[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['ZAG'], 'Num Zageiros'
	prob += lpSum([posLAT[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['LAT'], 'Num Lateraos'
	prob += lpSum([posMEI[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['MEI'], 'Num Meias'
	prob += lpSum([posATA[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['ATA']+0, 'Num Atacantes'
	prob += lpSum([posTEC[i]*jogadores_vars[i] for i in Jogadores]) == esquema[Esquema_Tatico]['TEC'], 'Num Tecnicos'

	#print prob

	# Resolve o problema
	#prob.solve()
	prob.solve(COIN(msg=0))

	# Imprime o status da resolucao
	#print "Status:", LpStatus[prob.status]

	#print precos.keys()
	soma_precos = 0.0
	soma_medias = 0.0

	#Exibe cada jogador escalado
	for variable in prob.variables():
	   nome_idx = variable.name[2:].replace("_"," ") #Macumba para obter nome
	   if variable.varValue: soma_precos += precos[nome_idx]
	   if variable.varValue: soma_medias += medias[nome_idx]
	   if not silencio and variable.varValue: print(variable.name, "==", variable.varValue, "$", precos[nome_idx], "%", medias[nome_idx])
	   #print variable.name, ">", variable.varValue
	
	if not silencio:
		print("A media conjunta esperada do time: %0.2f" % value(prob.objective))
		print("A soma dos precos: %0.2f" % soma_precos)
		print("A soma das medias: %0.2f" % soma_medias)
		print("")
	
	return soma_medias #Se for o caso, pode retornar value(prob.objective)
	
import sys
from pulp import *
import urllib.request, urllib.error, urllib.parse
import json

#Esquema_Tatico='4-3-3'
Preco_Maximo=100.00

esquema={'4-3-3':{'GOL':1, 'ZAG':2, 'LAT':2, 'MEI':3, 'ATA':3, 'TEC': 1 },
         '4-4-2':{'GOL':1, 'ZAG':2, 'LAT':2, 'MEI':4, 'ATA':2, 'TEC': 1 },
         '4-5-1':{'GOL':1, 'ZAG':2, 'LAT':2, 'MEI':5, 'ATA':1, 'TEC': 1 },
         '3-4-3':{'GOL':1, 'ZAG':3, 'LAT':0, 'MEI':4, 'ATA':3, 'TEC': 1 },
         '3-5-2':{'GOL':1, 'ZAG':3, 'LAT':0, 'MEI':5, 'ATA':2, 'TEC': 1 },
         '5-4-1':{'GOL':1, 'ZAG':3, 'LAT':2, 'MEI':4, 'ATA':1, 'TEC': 1 },
         '5-3-2':{'GOL':1, 'ZAG':3, 'LAT':2, 'MEI':3, 'ATA':2, 'TEC': 1 } }

response = urllib.request.urlopen('http://aposte.me/t/cartola__10.json')
data = json.load(response)   

#Seleciona todos os jogadores com Status Provável que participaram de pelo menos 3 jogos
obj_jogadores = [ jogador for jogador in data["jogadores"] if jogador['status']=='Provavel' and jogador['jogos']>=3 ]

Jogadores=[]
precos={}
medias={}
posGOL={}
posLAT={}
posZAG={}
posMEI={}
posATA={}
posTEC={}
#estavel={} #Parametro novo.

for j in obj_jogadores:
    nome=j['apelido']+'(' + j['clube']['abreviacao'] +')' + ' ' +j['posicao']['abreviacao']
	
    Jogadores+=[ nome ]
    #Jogadores.append( nome )
    precos[nome]=float(j['preco'])
    #medias[nome]=float(j['media']) #Tiro media diferente. Abaixo.
    posGOL[nome]=1 if j['posicao']['abreviacao']=='GOL' else 0
    posLAT[nome]=1 if j['posicao']['abreviacao']=='LAT' else 0
    posZAG[nome]=1 if j['posicao']['abreviacao']=='ZAG' else 0
    posMEI[nome]=1 if j['posicao']['abreviacao']=='MEI' else 0
    posATA[nome]=1 if j['posicao']['abreviacao']=='ATA' else 0
    posTEC[nome]=1 if j['posicao']['abreviacao']=='TEC' else 0
	
    #Calculando DP, Media, e quetais
    lista_jsons =  {"R05" : 'http://aposte.me/t/cartola__5.json',
	"R06" : 'http://aposte.me/t/cartola__6.json',
	"R07" : 'http://aposte.me/t/cartola__7.json',
	"R08" : 'http://aposte.me/t/cartola__8.json',
	"R09" : 'http://aposte.me/t/cartola__9.json',
	#"R10" : 'http://aposte.me/t/cartola__10.json',
	}
    puntos = [] #Guardo as pontuacoes de cada rodada, desse jogador
    for rodada in list(lista_jsons.keys()):
		responsex = urllib.request.urlopen(lista_jsons[rodada])
		datax = json.load(responsex) 
		for i in range(len(datax["jogadores"])):
			nomex = datax["jogadores"][i]['apelido']+'(' + datax["jogadores"][i]['clube']['abreviacao'] +')' + ' ' +datax["jogadores"][i]['posicao']['abreviacao']
			if nomex == nome :
				puntos.append( datax["jogadores"][i]["pontos"] )
    medias[nome]=-100.0 #Default
    if len(puntos) > 2:
		if pstdev( puntos ) != 0 and precos[nome] != 0:
			medias[nome] = mean(puntos)/(pstdev( puntos )*precos[nome])
	

#Cria uma variavel para cada jogador. 
#As variáveis são binárias: 1 se o jogador está escalado
#jogadores_vars = LpVariable.dicts("_",Jogadores,cat='Binary')
jogadores_vars = LpVariable.dicts("_",Jogadores,lowBound = 0,upBound = 1,cat='Integer')

#Adicionei uma lista de esquemas táticos. Para ver qual pode render mais
max_media = 0.0 #Maximo de retorno
max_esq = "" #Nome do melhor esquema tatico
for Esquema_Tatico in list(esquema.keys()):
	soma_medias = modelaCalcula(Esquema_Tatico,silencio=True) #Calculo retorno para o esquema tatico especifico
	
	#Avaliando esquema tatico que gera retorno maximo
	if( soma_medias > max_media ):
		max_esq = Esquema_Tatico
		max_media = soma_medias

#Ja com todos avaliados, agora roda mais uma vez, agora com o esquema otimo
soma_medias = modelaCalcula(max_esq, silencio=False)

 # -*- coding: utf-8 -*-
 
import urllib, json

def primeiraBandaPesquisaPorNome(trecho):
	#url = "http://api.vagalume.com.br/search.excerpt?q=vamos fugir&limit=10"
	url = "http://api.vagalume.com.br/search.excerpt?q="+ trecho +"&limit=3"
	response = urllib.urlopen(url.encode('utf-8'))
	data = json.loads(response.read())
	#print data
	#print "#Nome da musica:" + data["response"]["docs"][0]["title"] + " - Banda: " + data["response"]["docs"][0]["band"]
	#for d in data["response"]["docs"] :
	#	print "Nome da musica:" + d["title"] + " - Banda: " + d["band"]
	
	if data["response"]["numFound"] == 0 :
		print "Zica!"
	
	nome_musica = data["response"]["docs"][0]["title"]
	nome_banda = data["response"]["docs"][0]["band"]	
	return (nome_banda, nome_musica)
	
def ultimaPalavraUltimaLinha(nome_banda, nome_musica):
	url = "http://api.vagalume.com.br/search.php?art=" + nome_banda + "&mus=" + nome_musica
	response = urllib.urlopen(url.encode('utf-8'))
	data = json.loads(response.read())
	#print data["mus"][0]["text"]
	
	if data["type"] == "song_notfound" :
		print "Zica!"
	
	letra1 = data["mus"][0]["text"].split("\n") #\n ou \n\n
	letra = [l for l in letra1 if l != "" and l != u'[Refr\xe3o]'] #elimino linhas em branco
	#print letra
	
	from random import randint
	idx1 = randint(0,len(letra)-1) #Inclusive
	#print idx1
	#print letra[1]

	#return letra[-1].split(" ")[-1] #Ultima palavra da ultima linha
	#if letra[idx1].split(" ")[-1] == "":
	#	return letra[idx1].split(" ")[-2]
	return letra[idx1].split(" ")[-1] #Um toque de aleatoriedade
	
if __name__ == "__main__":
	#inicio = "Vamos Fugir"
	#nome_banda, nome_musica = primeiraBandaPesquisaPorNome(inicio)
	#ultima = ultimaPalavraUltimaLinha(nome_banda, nome_musica)
	ultima = "Vamos Fugir"
	for x in range(50):
		nome_banda, nome_musica = primeiraBandaPesquisaPorNome(ultima)
		ultima = ultimaPalavraUltimaLinha(nome_banda, nome_musica)
		print ultima + ",A:" + nome_banda + ",M:" + nome_musica
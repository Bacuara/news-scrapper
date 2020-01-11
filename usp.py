import requests
from bs4 import BeautifulSoup
import re

site = "https://jornal.usp.br/ciencias/ciencias-exatas-e-da-terra/na-era-do-gelo-chuvas-torrenciais-se-concentraram-no-nordeste-e-amazonia/"

result = requests.get(site).text

soup = BeautifulSoup(result,'html.parser')

tag = "Ciências Exatas"

#Obtém o título da notícia
title = soup.find("h1",{'class':'entry-title'})
title = re.sub(r'\<.*?\>','',str(title))

#Obtém a data da notícia
date = soup.find("time")

#Obtém o autor da notícia
author = soup.find("span",{'class',"vcard author author_name"})
author = re.sub(r'\<.*?\>','',str(author))
if author == None:
	print('Sem autor:' + title)

#Obtém a imagem principal da notícia
cover = soup.find("div",{'class':'post_content'}).find("img")
cover = str(cover["src"])
cover_description = soup.find("div",{'class':'post_content'}).find("em")
cover_description = str(cover_description)
#print(cover_description)

#Obtém o corpo da notícia
texto = soup.find("div",{'class':'csRow'})
texto = str(texto)

filename = ('exatas/' + re.sub("T.*$", "",date["datetime"]) + '-'
			+ title.replace(" ","-") + '.md')
myfile = open(filename,'w')

myfile.write('---\nlayout: post\ntitle: \"' + title + '\"\ndate:'	+ str(date["datetime"]) + '\nauthor:' + author +'\ncategorie: noticia\ntag:' + tag + '\nsource: Jornal da USP\nsource link:' + site + '\nimage:' + cover + '\n---\n![](' + cover + ')\n<p>' +  cover_description + '</p>\n' + texto)

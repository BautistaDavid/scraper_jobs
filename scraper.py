from bs4 import BeautifulSoup
import requests as rq
import pandas as pd

termino = input('Ingrese el termino que quiere Buscar:')
termino = termino.replace(' ','%20')

portal_empleo = f"https://www.elempleo.com/co/ofertas-empleo?&trabajo{termino}"
pag_ = rq.get(portal_empleo)

pag_portal = BeautifulSoup(pag_.text,'lxml')

titulos = []
links = []
info = []

for publicacion in pag_portal.find_all('h2',attrs={'class':'h4 item-title ee-mod'}):
    titulos.append(publicacion.a.get('title'))
    links.append('https://www.elempleo.com' + publicacion.a.get('href'))

resultados = pd.DataFrame()
resultados['Titulos'] = titulos
resultados['link'] = links

for sub_pub in resultados['link']:
    pag = BeautifulSoup(rq.get(sub_pub).text,'lxml')
    info.append(pag.find_all('div',attrs={'class':'description-block'})[0].find('span').text.strip())
resultados['info'] = info

resultados.to_csv('test.csv',index=False)
print(resultados.head(2))



from bs4 import BeautifulSoup
import requests
from lxml import etree

def buscar_datos():
    webpage=requests.get('https://coinmarketcap.com/')
    soup=BeautifulSoup(webpage.content,'html.parser')
    dom=etree.HTML(str(soup))
    total=[]

    primero_nombre=(dom.xpath('/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[3]/div/a/div/div/p/text()'))
    primero_precio=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[1]/td[4]/div/a/span/text()'))
    
    segundo_nombre=(dom.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[2]/td[3]/div/a/div/div/p/text()'))
    segundo_precio=(dom.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[2]/td[4]/div/a/span/text()'))

    tercera_nombre=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[3]/td[3]/div/a/div/div/p/text()'))
    tercera_precio=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[3]/td[4]/div/a/span/text()'))

    cuarta_nombre=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[4]/td[3]/div/a/div/div/p/text()'))
    cuarta_precio=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[4]/td[4]/div/a/span/text()'))

    quinto_nombre=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[5]/td[3]/div/a/div/div/p/text()'))
    quinto_precio=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[5]/td[4]/div/a/span/text()'))
    
    sexto_nombre=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[6]/td[3]/div/a/div/div/p/text()'))
    sexto_precio=(dom.xpath('/html/body/div/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr[6]/td[4]/div/a/span/text()'))

    total+=primero_nombre,primero_precio,segundo_nombre,segundo_precio,tercera_nombre,tercera_precio,cuarta_nombre,cuarta_precio,quinto_nombre,quinto_precio,sexto_nombre,sexto_precio

    return total



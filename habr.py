import requests
from bs4 import BeautifulSoup as BS
import os
import time



def pars(nom):
    count = 0

    page = []
    exx = []
    url = "https://habr.com/ru/all/page"+str(nom)
    request = requests.get(url)
    soup = BS(request.text, "html.parser")
    teme = soup.find_all("h2", class_='tm-article-snippet__title tm-article-snippet__title_h2')
    for temes in teme:
        temes = temes.find('a', {'class': 'tm-article-snippet__title-link'})
        sublink = temes.get('href')
        t = [str(temes.text),"https://habr.com" + str(sublink)]
        count += 1
        page.append(t)
    return page

def pars_serch(word):
    try:
        url ="https://habr.com/ru/all/"
        flag = "1"
        i = 0
        t = ""
        count = 0
        a = []
        exx=[]
        while count<3 :
            i+=1
            request = requests.get(url)
            soup = BS(request.text, "html.parser")
            teme = soup.find_all("h2", class_='tm-article-snippet__title tm-article-snippet__title_h2')
            for temes in teme:
                temes = temes.find('a', {'class': 'tm-article-snippet__title-link'})
                if str(word).upper() in str(temes.text).upper():
                    sublink = temes.get('href')
                    t =[str(temes.text), "https://habr.com" + str(sublink)]
                    if t not in a:
                        a.append(t)
                        count += 1
            if count <3:  url = 'https://habr.com/ru/all/page' + str(i + 1) + "/"
            else: return a
    except TimeoutError:
        return a

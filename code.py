from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import urllib.request
import json
import pandas as pd
import csv


# 利用colab云上编译
# 保存文件
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
# from google.colab import auth
# from oauth2client.client import GoogleCredentials

def url_load(url):
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url,None,headers = headers)
    #print(req)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features='lxml')
    centent = soup.find('div', {"class": "category-products"})
    b = centent.find_all('li')

    
    url_all = []
    name_all = []
    size_all = []
    prize_all = []

    

    for a in b:
        all_href = a.find_all('a',{"class":"product-image"})
        #print(all_href)
        for l in all_href:
            #print(l['href'])
            #list[] = l['href']
             
            e = l['href']

            u = printurl(e)
            url_all.append(u)
            #print(u)

            n = printname(e)
            name_all.append(n)

            s = printsize(e)
            size_all.append(s)

            p = printprize(e)
            prize_all.append(p)


    #print(au)
    data = {
        'url' : url_all,
        'name' : name_all,
        'size' : size_all,
        'prize' : prize_all
    }
    #print(data)

    #data_csv = pd.DataFrame(data)
    return data
    #data_csv.to_csv("data.csv",index=False,sep=',')
            
        #print(u)


def printurl(url):
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url,None,headers = headers)
    #print(req)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features='lxml')

    url_single = []
    #for i in range(1,24):
    url_single.append(url)
    #print(url_single)
    return url_single

    
    

def printname(url):
    #print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url,None,headers = headers)
    #print(req)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features='lxml')

    #<h1 class="product-name" itemprop="name">
    h = soup.find('h1',{"class":"product-name"})
    #print(h.get_text())
    name_single = []
    #for i in range(1,24):
    name_single.append(h.get_text())
    return name_single
        

    

    

def printsize(url):
    #print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url,None,headers = headers)
    #print(req)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features='lxml')

    
        

    #<span class="product-sizes__size">7*</span>
    s = soup.find_all('span',{"class":"product-sizes__size"})
    size_single = []
    for size in s:
      #print(size.get_text())
      size_single.append(size.get_text())
    return size_single


    

def printprize(url):
    #print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url,None,headers = headers)
    #print(req)
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, features='lxml')

    #<span class="product-sizes__price" data-selected-price>CN¥5,296.00</span>
    p = soup.find_all('span',{"class":"product-sizes__price"})
    #print(p.get_text())
    prize_single = []
    for prize in p:
        #print(prize.get_text())
        prize_single.append(prize.get_text())
    return prize_single
#def write_csv(content):



if __name__ == '__main__':
    
    # 以Air Jordan 1 为例
    url = 'https://www.stadiumgoods.com/air-jordan/air-jordan-1'
    
    x = url_load(url)
    data_csv = pd.DataFrame(x)
    data_csv.to_csv("data01.csv",index=False,sep=',')
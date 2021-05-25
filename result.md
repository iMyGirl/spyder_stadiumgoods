### colab平台试验记录-20190919

```python
代码单元格 <UoWyxPyQ9frz>
#%% [code]
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
import urllib.request
import json
import pandas as pd
import csv



#保存文件
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

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
            

            #u = printurl(e)
            print(e)
            url_single = []
            url_single.append(e)
            u = url_single

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
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # req = urllib.request.Request(url,None,headers = headers)
    # #print(req)
    # html = urllib.request.urlopen(req).read()
    # soup = BeautifulSoup(html, features='lxml')

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


def url_page(url,beginPage,endPage):
    for p in range(beginPage,endPage+1):
        fullurl = url + "/page/" + str(p)
        #print(fullurl)

        x = url_load(fullurl)
        
        data_csv = pd.DataFrame(x)
        #file_name = "data" + str(p) + ".csv"
        data_csv.to_csv('data.csv',index=False,sep=',')


        # Authenticate and create the PyDrive client.
        # This only needs to be done once in a notebook.
        auth.authenticate_user()
        gauth = GoogleAuth()
        gauth.credentials = GoogleCredentials.get_application_default()
        drive = GoogleDrive(gauth)
        # Create & upload a text file.
        #你想要导出的文件的名字
        uploaded = drive.CreateFile({'title': 'OK.csv'})
        #改为之前生成文件的名字
        uploaded.SetContentFile('data.csv')
        uploaded.Upload()
        print('Uploaded file with ID {}'.format(uploaded.get('id')))





#url_2 = "https://www.stadiumgoods.com/air-jordan/air-jordan-1/page/1"
if __name__ == '__main__':
    url = "https://www.stadiumgoods.com/air-jordan/air-jordan-1/page/1"
    #url_page(url,1,7)
    x = {}
    x = url_load(url)
    
    xyz = pd.DataFrame(x)
    xyz.to_csv('over.csv')
    

    # Authenticate and create the PyDrive client.
    # This only needs to be done once in a notebook.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)
    # Create & upload a text file.
    #你想要导出的文件的名字
    uploaded = drive.CreateFile({'title': 'OK.csv'})
    #改为之前生成文件的名字
    uploaded.SetContentFile('over.csv')
    uploaded.Upload()
    print('Uploaded file with ID {}'.format(uploaded.get('id')))
```
### 运行结果
>2019年9月19日 下午9:30的执行输出
	Stream
		https://www.stadiumgoods.com/air-jordan/air-jordan-1/page/1
		https://www.stadiumgoods.com/air-jordan-1-low-travis-scott-cq4277-001
		https://www.stadiumgoods.com/air-jordan-1-high-og-wmns-satin-black-toe-cd0461-016
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-obsidian-university-blue-555088-140
		https://www.stadiumgoods.com/air-jordan-1-retro-high-obsidian-university-blue-og-gs-575441-140
		https://www.stadiumgoods.com/air-jordan-1-high-og-defiant-yellow-cd6579-071
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-travis-scott-cd4487-100
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-defiant-couture-bq6682-006
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-la-to-chicago-court-purple-cd6578-507
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-554725-058-black-starfish-starfish-white
		https://www.stadiumgoods.com/air-jordan-1-low-black-toe-553558-116
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gym-red-555088-061
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-turbo-green-575441-311
		https://www.stadiumgoods.com/air-jordan-1-mid-yellow-toe-852542-071
		https://www.stadiumgoods.com/air-jordan-1-low-shattered-backboard-553558-128
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-555088-311-turbo-green-sail-white
		https://www.stadiumgoods.com/air-jordan-1-mid-obsidian-554724-174
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-554725-174-white-metallic-gold-obsidian
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-phantom-555088-160
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-rookie-of-the-year-555088-700
		https://www.stadiumgoods.com/air-jordan-1-low-royal-toe-cq9446-400
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-neutral-grey-hyper-crimson-555088-018
		https://www.stadiumgoods.com/air-jordan-1-mid-black-gold-patent-leather-852542-007
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-271466
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-crimson-tint-555088-081
		https://www.stadiumgoods.com/air-jordan-1-sb-retro-high-og-nyc-to-paris-light-bone-cd6578-006
		https://www.stadiumgoods.com/air-jordan-1-mid-shattered-backboard-554724-058
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-sports-illustrated-555088-015
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-050-black-dark-grey-black
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-554725-125-white-university-red-black
		https://www.stadiumgoods.com/air-jordan-1-low-gold-toe-cq94478-700
		https://www.stadiumgoods.com/air-jordan-1-retro-high-off-white-unc-aq0818-148
		https://www.stadiumgoods.com/air-jordan-1-low-gs-cq9487-700-metallic-gold-black-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-royale-2017-555088-007
		https://www.stadiumgoods.com/air-jordan-1-low-mystic-green-553558-113
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-555112-190-white-rose-gold-black
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-unc-patent-leather-cd0461-401
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-nrg-256843
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-062-black-cone-light-bone
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-051-black-dark-concord-white
		https://www.stadiumgoods.com/air-jordan-1-low-cj9216-051-black-field-purple-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gym-red-gs-575441-061
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-061-black-infrared-23-white
		https://www.stadiumgoods.com/air-jordan-1-low-gs-553560-116-white-black-gym-red
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-nrg-861428-061-black-university-red-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-crimson-tint-575441-081
		https://www.stadiumgoods.com/air-jordan-1-mid-se-gs-bq6931-007-black-metallic-gold-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-575441-602-gym-red-black-white-photo-blue
		https://www.stadiumgoods.com/air-jordan-1-low-royal-toe-gs-cq9486-400
		https://www.stadiumgoods.com/air-jordan-1-mid-white-black-bq6472-101
		https://www.stadiumgoods.com/air-jordan-1-low-gs-553560-128-white-black-starfish
		https://www.stadiumgoods.com/air-jordan-1-low-university-gold-553558-127
		https://www.stadiumgoods.com/wmns-air-jordan-1-retro-low-ns-ah7232-100-white-metallic-gold-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-575441-401-hyper-royal-sail-hyper-royal
		https://www.stadiumgoods.com/air-jordan-1-mid-lakers-2019-852542-700
		https://www.stadiumgoods.com/nike-air-jordan-1-low-sb-eric-koston-cj7891-401
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-125-white-university-red-black
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-121-white-metallic-silver-black
		https://www.stadiumgoods.com/jordan-1-mid-554724-116-white-black-gym-red
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-575441-015-black-varsity-red-sail
		https://www.stadiumgoods.com/air-jordan-1-mid-top-3-gs-bq6931-005
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-bg-248848
		https://www.stadiumgoods.com/jordan-1-retro-high-555088-610-red-black-white
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-124-white-black-hyper-royal
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-113-white-black-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-nigel-sylvester-bv1803-106
		https://www.stadiumgoods.com/air-jordan-1-retro-high-off-white-white-aq0818-100
		https://www.stadiumgoods.com/air-jordan-1-retro-high-pine-green-555088-302
		https://www.stadiumgoods.com/wmns-air-jordan-1-retro-low-ns-ah7232-011-black-metallic-gold-white
		https://www.stadiumgoods.com/air-jordan-1-mid-se-852542-306-turbo-green-black-hyper-pink
		https://www.stadiumgoods.com/air-jordan-1-mid-se-852542-301-pine-green-black-sail
		https://www.stadiumgoods.com/air-jordan-1-low-hyper-pink-553558-119
		https://www.stadiumgoods.com/air-jordan-1-retro-court-purple-555088-501
		https://www.stadiumgoods.com/air-jordan-1-mid-se-852542-801-crimson-tint-hyper-pink-black
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-gs-575441-160-sail-black-phantom-gym-red
		https://www.stadiumgoods.com/air-jordan-mid-1-all-over-logos-gs-554725-143
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-bv7446-400-blue-void-clear-team-royal
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-555088-801-guava-ice-sail
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-554725-116-white-black-gym-red
		https://www.stadiumgoods.com/air-jordan-1-mid-554724-115-white-black-wolf-grey
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-555088-401-hyper-royal-sail
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-555112-300-green-abyss-frosted-spruce
		https://www.stadiumgoods.com/air-jordan-1-retro-high-union-storm-blue-bv1300-146
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-271456
		https://www.stadiumgoods.com/air-jordan-1-mid-bq6578-001-black-university-red-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-twist-panda-cd0461-007
		https://www.stadiumgoods.com/air-jordan-1-mid-se-852542-400-deep-royal-blue-black
		https://www.stadiumgoods.com/air-jordan-1-retro-high-union-black-toe-bv1300-106
		https://www.stadiumgoods.com/air-jordan-1-mid-bq6578-100-white
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-bg-248850
		https://www.stadiumgoods.com/air-jordan-1-mid-se-852542-010-black-black-sail-wolf-grey
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-ice-blue-555112-104
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-spider-man-origin-story-555088-602
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-bg-248849
		https://www.stadiumgoods.com/air-jordan-1-retro-high-og-clay-green-555088-135
		https://www.stadiumgoods.com/wmns-air-jordan-1-high-og-nrg-bv2613-600-bordeaux-lt-armory-blue
		https://www.stadiumgoods.com/air-jordan-1-mid-gs-554725-061-black-infrared-23-white
		Uploaded file with ID 19Yw-fgKevLDNFQOWFeALZU8ZuweQ9_sv

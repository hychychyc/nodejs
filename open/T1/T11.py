from selenium import webdriver
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import time
import re
from itertools import chain
import requests

times=time.time()
options=webdriver.FirefoxOptions()
options.add_argument('-headless')
# 声明浏览器对象
url="https://www.bilibili.com/v/popular/rank/all?spm_id_from=333.851.b_7072696d61727950616765546162.3"
driver = webdriver.Firefox(options=options)
driver.get(url) 
html2 = driver.page_source
#h=re.findall(r'<li class="rank-item" data-id="(.*?)" data-rank',html2)
#h2=re.findall(r'<img class="lazy-image cover" data-src="(.*?)"',html2)
#h2=re.findall(r'<img class="lazy-image cover" data-src="(.*?)"',html2)             457.4万
#elemt = browser.find_element_by_xpath(r'//*[@id="xpathname"]')
h=driver.find_elements_by_xpath("//*//li[@class='rank-item']")
h2=driver.find_elements_by_xpath("//*//img[@class='lazy-image cover']")
h3=driver.find_elements_by_xpath("//*//span[@class='data-box']")
h4=driver.find_elements_by_xpath("//*//span[@class='data-box up-name']")
f=open("ans10.txt","w",encoding='utf-8')
h5={}
h6={}
h7={}
h8={}
h9={}
h10={}
t=1
p=0
for a in h3:
    if(t&1):
        h5[p]=a.text
    else:
        h6[p]=a.text
        p+=1
    t+=1
t=0
for a in h:
    h7[t]=a.get_attribute("data-rank")
    h10[t]=a.get_attribute("data-id")
    t+=1
t=0
for a in h2:
    h8[t]=a.get_attribute("data-src")
    t+=1
t=0
for a in h4:
    h9[t]=a.text
    t+=1
for i in range(t):
    f.write(str (h5[i])+"  "+str (h6[i])+"  "+str(h10[i])+"  "+str(h7[i])+"  "+str(h8[i])+"  "+str(h9[i])+'\n')
f.close
    #print(elem.text)
    #print(elem.get_attribute("src"))
#
#/html/body/div[3]/div[2]/div[2]/ul/li[1]/div[2]/div[2]/div[1]/span[1]/i
print("共耗时:",end=" ")
print(time.time()-times)


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
p=100
f=open("ans14.txt","w",encoding='utf-8')
for i in range(0,p):
    try:
        tmp=driver.find_elements_by_xpath("//*//a[@class='title']")
        w=tmp[i]
        w.click()
        time.sleep(3)
        windows=driver.window_handles
        driver.switch_to.window(windows[1])
        #time.sleep(3)
        h=driver.find_element_by_xpath("//*//div[@class='info']")
        #time.sleep(2)
        h2=driver.find_elements_by_xpath("//*//li[@class='tag']")
        #time.sleep(2)
        h3=driver.find_element_by_xpath("//*//span[@class='like']")
        h4=driver.find_element_by_xpath("//*//span[@class='coin']")
        h5=driver.find_element_by_xpath("//*//span[@class='collect']")
        h6=driver.find_element_by_xpath("//*//span[@class='share']")
        #print(h.text)
        f.write(str(h.text)+"  "+str(h3.text)+"  "+str(h4.text)+"  "+str(h5.text)+"  "+str(h6.text)+"  "+'\n')
        for j in h2:
            f.write(str(j.text)+"  ")
        f.write("\n")
        #time.sleep(3)
        driver.close()
        driver.switch_to.window(windows[0])
        #driver.back()
        time.sleep(3)
    except:
        try:
            tmp=driver.find_elements_by_xpath("//*//a[@class='title']")
            w=tmp[i]
            w.click()
            time.sleep(3)
            windows=driver.window_handles
            driver.switch_to.window(windows[1])
            #time.sleep(3)
            h=driver.find_element_by_xpath("//*//div[@class='info open']")
            #time.sleep(2)
            h2=driver.find_elements_by_xpath("//*//li[@class='tag']")
            #time.sleep(2)
            h3=driver.find_element_by_xpath("//*//span[@class='like']")
            h4=driver.find_element_by_xpath("//*//span[@class='coin']")
            h5=driver.find_element_by_xpath("//*//span[@class='collect']")
            h6=driver.find_element_by_xpath("//*//span[@class='share']")
            print(h3.text)
            f.write(str(h.text)+"  "+str(h3.text)+"  "+str(h4.text)+"  "+str(h5.text)+"  "+str(h6.text)+"  "+'\n')
            for j in h2:
                f.write(str(j.text)+"  ")
            f.write("\n")
            #time.sleep(3)
            driver.close()
            driver.switch_to.window(windows[0])
        #driver.back()
            time.sleep(3)
        except:
            driver.switch_to.window(windows[0])
            print("error")
    print(i)
    
driver.quit()
f.close

print("共耗时:",end=" ")
print(time.time()-times)


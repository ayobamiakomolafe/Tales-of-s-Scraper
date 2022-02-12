import requests
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
item_attr=list()
for i in range(1,10):
    webpage='https://www.calibrefurniture.com.au/collections/pre-order?' + 'page=' + str(i)
    d.get(webpage)
    items=d.find_elements_by_class_name("product-item ")
    
    for item in items:
        attr=list()
        item_name=item.find_element_by_tag_name("h3").text
        attr.append(item_name)
        link=item.find_element_by_tag_name("a")
        href=link.get_attribute('href')
        attr.append(href)
        item_attr.append(attr)
   
    
df=pd.DataFrame(item_attr)
df.to_csv('item_attributes')







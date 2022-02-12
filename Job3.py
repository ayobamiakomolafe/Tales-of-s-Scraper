import pandas as pd
import requests
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("--headless")
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
import time
#options=chrome_options
df=pd.read_csv('office')
links=df['1'].tolist()

Number=None
for link in links[126:]:
    item_attr=list()
    Number=links.index(link)
    print(Number)
    webpage=link
    d.get(webpage)
    if Number==126:
        d.find_element_by_link_text('login').click()
        email = d.find_element_by_id("customer_email")
        password=d.find_element_by_id("customer_password")
        email.send_keys('info@rumaliving.com.au')
        time.sleep(10)
        password.send_keys('zicrew-qadwu8-bihWon')
        time.sleep(5)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        try:
            try:
                cart=d.find_element_by_class_name("add-to-cart__text")
                cart.click()
            except:
                WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@data-pre-order-atc-button='1']")))  
                b=d.find_element_by_xpath("//button[@data-pre-order-atc-button='1']")
                d.execute_script("arguments[0].click();", b)
        except:
             continue
            
        wait = WebDriverWait(d, 10)
        zips=[3000, 2000, 6000, 2600, 4000, 5000, 7000]
        states=['Victoria', 'New South Wales', 'Western Australia','Australian Capital Territory', 'Queensland', 'South Australia', 'Tasmania']
        
        for a, b in zip(states, zips):
            costs=list()
            costs.append(Number)
            costs.append(a)
            
            x="//select[@id='address_province']/option[@value=" + "'" + a + "'" + "]"
            element = wait.until(EC.element_to_be_clickable((By.XPATH, x)))
            d.find_element_by_xpath(x).click()
            java="document.getElementById('address_zip').value='{}'".format(b)
            d.execute_script(java)
            d.find_element_by_xpath("//input[@value='Calculate shipping']").click()
            WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.ID, "shipping-rates"))
                )
            text=d.find_element_by_id("shipping-rates").text
            costs.append(text)
            item_attr.append(costs)
        WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Remove item from cart']")))    
       
        d.find_element_by_xpath("//a[@title='Remove item from cart']").click() 
        


    else:
        try:
            try:
                cart=d.find_element_by_class_name("add-to-cart__text")
                cart.click()
            except:
                WebDriverWait(d, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@data-pre-order-atc-button='1']")))  
                b=d.find_element_by_xpath("//button[@data-pre-order-atc-button='1']")
                d.execute_script("arguments[0].click();", b)
        except:
            continue

        wait = WebDriverWait(d, 10)
        zips=[3000, 2000, 6000, 2600, 4000, 5000, 7000]
        states=['Victoria', 'New South Wales', 'Western Australia','Australian Capital Territory', 'Queensland', 'South Australia', 'Tasmania']
            
        for a, b in zip(states, zips):
            costs=list()
            costs.append(Number)
            costs.append(a)
            x="//select[@id='address_province']/option[@value=" + "'" + a + "'" + "]"
            element = wait.until(EC.element_to_be_clickable((By.XPATH, x)))
            d.find_element_by_xpath(x).click()
            java="document.getElementById('address_zip').value='{}'".format(b)
            d.execute_script(java)
            d.find_element_by_xpath("//input[@value='Calculate shipping']").click()
            WebDriverWait(d, 10).until(
            EC.presence_of_element_located((By.ID, "shipping-rates"))
                )
            text=d.find_element_by_id("shipping-rates").text
            costs.append(text)
            item_attr.append(costs)
        WebDriverWait(d, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Remove item from cart']"))
           )
        d.find_element_by_xpath("//a[@title='Remove item from cart']").click() 

    df3=pd.read_csv('Office.csv')
    df2=pd.DataFrame(item_attr, columns=['ID','State','Cost'])
    df4=pd.concat([df3,df2])
    df4.to_csv('Office.csv', sep = ',', index = False)      
      
        







        
        
        
    

    
      
        

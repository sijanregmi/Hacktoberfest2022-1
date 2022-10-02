import pandas as pd
import os

items = pd.read_csv(r"C:\Users\ankit\Desktop\food item list.csv")
items = items["Food Items"].tolist()    # Converting DataFrame into list
  
root_path = "D:\\Foodify\\"      # Folder Path
  
for item in items:
    path = os.path.join(root_path, item)
    os.mkdir(path)

#import Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import keyboard
import os
import time

for i in items[10:100]:

    browser = webdriver.Chrome(r'C:\Selenium\chromedriver.exe')
    browser.get('https://www.google.com/search?q='+str(i)+'&source=lnms&tbm=isch')
    folder = ("D:/Foodify/"+str(i)+"/")


    # Open first 100 images except 25,50,75,100(non-image)
    for j in range(1,26):
        if j%25==0:
            continue
        #xPath="""//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img"""
        browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(j)+']/a[1]/div[1]/img').screenshot(folder+ '(' + str(j) + ').jpg')
        time.sleep(0.3)    
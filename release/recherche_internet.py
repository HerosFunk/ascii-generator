import os

try:
     from selenium import webdriver
except ModuleNotFoundError:
     os.system("pip install --config-settings=\"--prefix={}\" selenium"
               .format(os.path.join("./", "_depedencies")))
     from selenium import webdriver
     

import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import shutil



def recherche():
    mot_a_rechercher = input("Que voulez-vous recherchez ?  ")
    url = 'https://www.google.com/search?q='+str(mot_a_rechercher)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'

    driver = webdriver.Chrome()
    str1 = driver.capabilities['browserVersion']
    str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

    if str1[0:2] != str2[0:2]: 
      print("please download correct chromedriver version")
    
    nom, img = url_img(url,driver,mot_a_rechercher)
    save_img(img,nom)
    return nom
    
def url_img(url,driver,mot):
    """
    Cherche l'image sur internet correspondant au nom et au numéro de l'image que l'on souhaite
    grâce à son xpath
    """
    
    driver.get(url)
    acceptCookiesUrl = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/div[3]')
    
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/div[3]'))))
    
    time.sleep(1)
    
     
    n = int(input("Quelle image souhaitez-vous prendre?(entier attendu)"))
        
    
    imgurl = driver.find_element('xpath', '//*[@id="islrg"]/div[1]/div['+str(n)+']/a[1]')
                                            
    time.sleep(2)                         
                                          
                                                                                
    imgurl.click()
    time.sleep(2)
    
    img = driver.find_element('xpath', '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]').get_attribute("src")
                                                                     
                                               
                                        
    print(img)

    driver.close()
    nom = mot + '_' + str(n)
    
    return nom, img                                                                                                                                       


def save_img(img,nom):
    try:

        image_path = nom +'.jpg'
        
        requete = requests.get(img,stream=True)
        
        
        
            
        shutil.copyfileobj(requete.raw, open(image_path, 'wb'))
        
        
    except Exception:
        
        pass
    
    
            


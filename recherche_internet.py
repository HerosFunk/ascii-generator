from selenium import webdriver
import time
import requests
import shutil



def recherche():
    mot_a_rechercher = input("Que voulez-vous recherchez ?  ")
    url = 'https://www.google.com/search?q='+str(mot_a_rechercher)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'

    driver = webdriver.Chrome()
    
    nom, img = url_img(url,driver,mot_a_rechercher)
    save_img(img,nom)
    return nom
    
def url_img(url,driver,mot):
    """
    Cherche l'image sur internet correspondant au nom et au numéro de l'image que l'on souhaite
    grâce à son xpath
    """
    
    driver.get(url)    
    time.sleep(1)
     
    n = int(input("Quelle image souhaitez-vous prendre?(entier attendu)"))
        
    
    imgurl = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(n)+']/a[1]')
    time.sleep(2)                         
                                          
                                                                                
    imgurl.click()
    time.sleep(2)
    
    img = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
                                                                             
                                               
                                        
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
    
    
            


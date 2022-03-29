########################  ASCII ART / PROJECT DE NOEL  #####################


'by  Léo / Léo / Mohamed / Louis'




###################   Importation des modules   ##############################

import os
import time
import PIL.Image
import recherche_internet



################################################################
def ascii_art():
    
    image, nom_image = demander()
    
    
    nouvelle_image = redimensionner(image)
    
    image_noir_et_blanc = noir_et_blanc(nouvelle_image)

    
    
    ascii_str = pixel_en_ascii(image_noir_et_blanc)

    
    
    mise_en_forme(image_noir_et_blanc, ascii_str, nom_image)
    
    ouvrir(nom_image)
    
    
    
##################################################################
    
def demander():
    demande = True
    while demande == True:
        type_recherche = input("Quel type de recherche voulez-vous faire?(1, 2 ou 3) \n \n 1. Recherche d'une image sur internet \n\n 2. Importation d'une image \n\n 3. Superposer deux images \n")
        if type_recherche == '1':
            
            nom_image = recherche_internet.recherche()
            demande = False
            path = nom_image + '.jpg'
        
             
    
        elif type_recherche == '2':
            
            path = input("Entrer le chemin de votre image: ")
            ''' supprime l'extension de l'image'''
            nom_image = os.path.splitext(path)[0]
            
            demande = False
            
        elif type_recherche == '3':
            
            image = input("Entrer le chemin de votre image à superposer: ")
            image_fond = input("Entrer le chemin de votre fond: ")
            
            image_s = PIL.Image.open(image)
            fond = PIL.Image.open(image_fond)
            
            nom_image = os.path.splitext(image)[0] + '+' + os.path.splitext(image_fond)[0]
            path = nom_image + ".jpg"
            superposer(image_s,fond,nom_image)
            
            demande = False
            
        else:
            
            print("\nErreur de sélection. Veuillez réesayer.\n")
            time.sleep(1)
        
        
        
        
    try:
        
        image = PIL.Image.open(path)
        
    except:
    
        print(path, "Impossible de trouver l'image ")
        
    return image, nom_image

############# Conversion ###############
def redimensionner( image, nouvelle_largeur = 800):
    '''Nous devons convertir l'image en une largeur et une hauteur réduites afin qu'elle ne donne pas de texte de grande taille
       car la taille d'un caracteres ascii est plus grande qu'un pixel
       800 -> largeur par défaut modifiable
    '''
    (largeur, hauteur) = image.size

    ''' on recupere la hauteur et la largeur de l'image avec la bibliotheque PIL'''
    ratio = hauteur/largeur/1.65

    nouvelle_hauteur = int(nouvelle_largeur * ratio)

    ''' On calcule la nouvelle hauteur'''
    
    nouvelle_image = image.resize((nouvelle_largeur ,nouvelle_hauteur))
    '''on utilise la bibliotheque PIL pour redimmensionner l'image avec la haute et la largeur calculées'''
    
    return nouvelle_image


def noir_et_blanc(image):
    return image.convert('L')
''' on utilise la methode de la biblio PIL avec l'option L pour convertir en noir et blanc '''


def pixel_en_ascii(image):
    caracteres_ascii = [ "@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += caracteres_ascii[pixel//25]
    return ascii_str


##################################################################
def mise_en_forme(image, caracteres,name):
    largeur_image = image.width
    
    longueur_chaine = len(caracteres)
    image_ascii= ""
    for i in range(0, longueur_chaine, largeur_image):
        image_ascii += caracteres[i:i+largeur_image] + "\n"
    ##sauvegarde
    try :
        open('ascii_' + name +".txt", "w").write(image_ascii)
    except:
        open("image_ascii.txt", "w").write(image_ascii)

def ouvrir(name):
    try:
        os.startfile( name + '.jpg')
    except:
        os.startfile( name + '.png')
        
            
    time.sleep(1)
    try:        
        os.startfile('ascii_' + name +".txt")
    except:
        os.startfile("image_ascii.txt")
        
#########################
        
        
def superposer(image,fond,nom):


    
    image = redimensionner(image,400)
    fond = redimensionner(fond, 800)
    
    
    
    (largeur_img, hauteur_img) = image.size
    (largeur_fond, hauteur_fond) = fond.size
    fond.paste(image, ((largeur_fond-largeur_img)//2,(hauteur_fond-hauteur_img)//2), image)
    fond.save(nom +".jpg","JPEG")
    
    


def main():
    
    ascii_art()

    
    
    
    
    


if __name__ == "__main__":
    main()

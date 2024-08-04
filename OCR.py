from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import imageio as iio
import pytesseract
import cv2
import nitk
import nltk
from nltk import tokenize
#import camera_shot 

#def shot():
 #   camera_shot.shot() 


drug = ['Panadol','Catafast','Arythrex', 'Dantrelax comp', 'Rx']
drugFound = []
def ocr():
    
    #Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    #image = askopenfilename()
    image = r"image.jpg"
    
    text = pytesseract.image_to_string(Image.open(image))
    tokenizer = nltk.tokenize.WhitespaceTokenizer ()
    tokenizer.tokenize (text)
    tokenizer = nltk.tokenize.WordPunctTokenizer ( )
    tokenizer.tokenize (text)
    if "Catafast" in text:
        drugFound.append(drug[1])
    if "Panadol" in text:
        drugFound.append(drug[0])
    if 'Arythrex' in text:
        drugFound.append(drug[2])
    if 'Dantrelax comp' in text:
        drugFound.append(drug[3])
    if 'Rx' in text:
        drugFound.append(drug[5])
    if 'Bola' in text:
        drugFound.append('Bola')
    return drugFound
    
    #cheack the medcine
def cheack():
        
        print("is {} what u want?\n0 = no\n1=yes".format(drugFound))
        ans = int(input())
        if ans == 1:
            print("drug is despatching please wait ...")
        else:
            print("please insert the presecreption again")
            #shot()
            #chooseImg()
            return 0
ocr()
cheack()





    





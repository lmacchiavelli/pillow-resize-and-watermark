from PIL import Image
import glob, os

#tupla news w h

# (original height / original width) x new width = new height


#newsH = im.sizew = im.size[0] / im.size[1] * 230

#new Height = original width / original height * new width


#offset = 230 / 2;



#img2 = img.crop((100, 0, 230, 200))

#img2.save("mini3.jpg")


def croppa_immagine(imgSpec,nome):
    """ 
    Accetta una Tupla con queste impostazioni es:
    (230, 200,"fiori1.jpg","-immagine-media",True) tradotta:
    (width finale, height finale, "url immagine sorgente", "prefisso da
    aggiungere al nome finale dell'immagine ad esempio -big", Watermark true false)
    per dimensionare l'immagine
    l'immagine originale viene portata all'altezza dell'immagine
    risultante secondo questa formula :
    NewHeight = original width / original height * new width
    poi viene croppata portandosi al centro calcolando l'offset

    """
    #Apertura
    im        = Image.open(imgSpec[2])
    newsH     = im.size[0] / im.size[1] * imgSpec[0]
    img       = im.resize((int(newsH),imgSpec[0]))
    #Calcolo Offset
    imgCenter = img.size[0] / 2
    resCenter =  imgSpec[0] / 2
    offset    =   imgCenter - resCenter
    #Assegno a una tupla
    imgResult = (int(offset),0,int(imgSpec[0]+offset),imgSpec[1])
    #Applico il crop all'immagine
    img = img.crop(imgResult)
    #Salvo il file
    

    #APPLICO WATERMARK
    if imgSpec[4]:
        watermark = Image.open('filigrana.png')
        img.paste(watermark, (10, 10), watermark)


    salva(img,nome+imgSpec[3])
    
def salva(imgObject,nome):
    imgObject.save (nome + ".jpg", optimize=True, quality=100, compression="lossless")


imnews = 230, 200,"fiori1.jpg","fiori-colorati-tulipani"

dimensioni = [
    ( 230 , 200 , "fiori1.jpg" , "-medium"     , True  ),
    ( 220 , 100 , "fiori1.jpg" , "-mini"       , False ),
    ( 400 , 400 , "fiori1.jpg" , "-big-square" , True  ),
    ( 60  ,  60 , "fiori1.jpg" , "-mini"       , False ),
]


#croppa_immagine(imnews)

for i in dimensioni:
    croppa_immagine(i,"fiori-coloratissimi")



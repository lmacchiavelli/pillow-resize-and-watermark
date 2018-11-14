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
    Accept a Tupla with these settings eg:
    (230, 200, "fiori1.jpg", "- image-media", True) translated:
    (final width, final height, "source image url", "prefix by
    add to the final image name such as -big ", Watermark true false)
    to dimension the image
    the original image is brought to the height of the image
    resulting from this formula:
    NewHeight = original width / height height * new width
    then it is cropped by moving to the center by calculating the offset

    """
    #Opening the file
    im        = Image.open(imgSpec[2])
    newsH     = im.size[0] / im.size[1] * imgSpec[0]
    img       = im.resize((int(newsH),imgSpec[0]))
    #calculate the offset
    imgCenter = img.size[0] / 2
    resCenter =  imgSpec[0] / 2
    offset    =   imgCenter - resCenter
    #Assign a tuple
    imgResult = (int(offset),0,int(imgSpec[0]+offset),imgSpec[1])
    #Apply IMG Crop
    img = img.crop(imgResult)
    #File saving
    

    #APPLY WATERMARK
    if imgSpec[4]:
        watermark = Image.open('filigrana.png')
        img.paste(watermark, (10, 10), watermark)


    salva(img,nome+imgSpec[3])
    
def salva(imgObject,nome):
    imgObject.save (nome + ".jpg", optimize=True, quality=100, compression="lossless")


imnews = 230, 200,"fiori1.jpg","fiori-colorati-tulipani"

image_to_crop_and_optimize = [
    ( 230 , 200 , "fiori1.jpg" , "-medium"     , True  ),
    ( 220 , 100 , "fiori1.jpg" , "-mini"       , False ),
    ( 400 , 400 , "fiori1.jpg" , "-big-square" , True  ),
    ( 60  ,  60 , "fiori1.jpg" , "-mini"       , False ),
]

for i in image_to_crop_and_optimize:
    croppa_immagine(i,"fiori-coloratissimi")

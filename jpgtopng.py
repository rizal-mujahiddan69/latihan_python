from PIL import Image
import cv2

# alamat directory
folderku = input("Directorymu : ")

if(folderku[len(folderku)-1] != '/'):
    folderku += "/"

# nama file disertai extensinya
fileku = input("Filenya : ")

# alamat seluruhnya dataku
dataku = folderku+fileku

# Buka Gambarnya
im1 = Image.open(dataku)
filesave = fileku.split('.')[0] + '.png'
im1 = im1.resize((300, 200))
im1.save(folderku+filesave)

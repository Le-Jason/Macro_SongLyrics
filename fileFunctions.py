import os
from PIL import Image, ImageTk


def myImage(name,width,height):
    #Function that imports images
    #Input:Name of file(no .(whatever)), Wanted Width, Wanted Height
    #Output:Image object
    file = os.path.join("Assets",name+".png")
    imageOpen = Image.open(file)
    resizeImage = imageOpen.resize((width,height))
    usedImage = ImageTk.PhotoImage(resizeImage)
    return usedImage
def clearHotKey():
    #Clear keybind from all files
    #Input:keybind.txt
    #Output:N/A
    fileName = os.path.join("Data","Settings","keybind.txt")
    title = []
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            title.append(templine[0])
    with open(fileName,'w',encoding="utf-8") as wf:
        for j in range(0,len(title)):
            tempWord = title[j] + " " + " " + " " + " " + "\n"
            wf.write(tempWord)
def sub():
    #test function
    pass
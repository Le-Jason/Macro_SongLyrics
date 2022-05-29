from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os 
import pyautogui
import pydirectinput
import keyboard 
import random
import threading

pyautogui.PAUSE = 0.01
global x
x = False

class voiceEvent:
    def __init__(self,text,key,serial):
        self.text = text
        self.key = key
        self.serial = serial
        self.idx = 0
    def trigger(self):
        if self.key != None:
            if keyboard.is_pressed(self.key):
                while(keyboard.is_pressed(self.key)):
                    pass
                
                if self.serial == False:
                    voiceEvent.randomLeaugeEvent(self)
                else:
                    voiceEvent.serialLeagueEvent(self)
                    self.idx += 1
            pyautogui.keyUp('shift')
        else:
            pass
    def randomLeaugeEvent(self):
        fileName = os.path.join("Data","HotkeyEvents",self.text)
        
        with open(fileName,'r',encoding="utf-8") as f:
            f_content = f.readlines()
            idx = random.randint(0,len(f_content)-1)
            pydirectinput.press('enter')
            pyautogui.write('/all ')
            pyautogui.write(f_content[idx])
    def serialLeagueEvent(self):
        fileName = os.path.join("Data","HotkeyEvents",self.text)
        with open(fileName,'r',encoding="utf-8") as f:
            f_content = f.readlines()
            if self.idx >= len(f_content):
                self.idx = 0
            pydirectinput.press('enter')
            pyautogui.write('/all ')
            pyautogui.write(f_content[self.idx])

def sub():
    print(1)

def showFrame(frame):
    frame.tkraise()

def getFileList(frame):
    textName = hotkeyFrame_Listbox.get(hotkeyFrame_Listbox.curselection())
    titleString.set(textName)
    fileName = os.path.join("Data","Settings","keybind.txt")
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            if(textName == templine[0]):
                try:
                    keyString.set(templine[1])
                    serialString.set(templine[2])
                except:
                    keyString.set("N/A")
                    serialString.set("N/A")
    frame.tkraise()

def openFile():
    filepath = filedialog.askopenfilename(filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    try:
        newfilename = os.path.basename(filepath)
        newfilepath = os.path.join("Data","HotkeyEvents",newfilename)
        with open(filepath,'r',encoding="utf-8") as rf:
            with open(newfilepath,'w') as wf:
                for line in rf:
                    wf.write(line)
        hotkeyFrame_Listbox.insert(1,newfilename)
        os.remove(filepath)
    except:
        pass

def myImage(name,width,height):
    file = os.path.join("Assets",name+".png")
    imageOpen = Image.open(file)
    resizeImage = imageOpen.resize((width,height))
    usedImage = ImageTk.PhotoImage(resizeImage)
    return usedImage

def keyChange():
    keyName = changekeyFrame_KeyEntry.get()
    fileName = os.path.join("Data","Settings","keybind.txt")
    title = []
    keys = []
    serial = []
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            title.append(templine[0])
            try:
                keys.append(templine[1])
                serial.append(templine[2])
            except:
                keys.append(None)
                serial.append(None)
    for i in range(0,len(title)):
        if(title[i] == titleString.get()):
            keys[i] = keyName
            serial[i] = "Serial"
            keyString.set(keyName)
            serialString.set("Serial")
    with open(fileName,'w') as wf:
        for j in range(0,len(title)):
            try:
                tempWord = title[j] + " " + keys[j] + " " + serial[j] + "\n"
            except:
                tempWord = title[j] + " " + " " + " " + " " + "\n"
            wf.write(tempWord)

def serialChange():
    fileName = os.path.join("Data","Settings","keybind.txt")
    title = []
    keys = []
    serial = []
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            title.append(templine[0])
            try:
                keys.append(templine[1])
                serial.append(templine[2])
            except:
                keys.append(None)
                serial.append(None)
    for i in range(0,len(title)):
        if(title[i] == titleString.get()):
            if serial[i] == "Serial":
                serial[i] = "Random"
                serialString.set("Random")
                changekeyFrame_SerialButton.config(text = "Change:Serial")
            else:
                serial[i] = "Serial"
                serialString.set("Serial")
                changekeyFrame_SerialButton.config(text = "Change:Random")
    with open(fileName,'w') as wf:
        for j in range(0,len(title)):
            try:
                tempWord = title[j] + " " + keys[j] + " " + serial[j] + "\n"
            except:
                tempWord = title[j] + " " + " " + " " + " " + "\n"
            wf.write(tempWord)

def play():
    global x 
    if x:
        x = False
        mainFrame_StartButton.config(text = "Play",
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    image=playimg,
                    compound="left",
                    padx=5)
    else:
        x = True
        mainFrame_StartButton.config(text = "Stop",
                    font=("Arial",30),
                    fg="red",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    image=stopimg,
                    compound="left",
                    padx=5)
    thread = threading.Thread(target=mainProgram)
    thread.daemon = True
    if x:
        thread.start()
    print("Threads Active:",threading.activeCount())

def mainProgram():
    global x
    filename = os.path.join("Data","Settings","keybind.txt")
    listEvent = []
    title = []
    keys = []
    with open(filename,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            title.append(templine[0])
            try:
                keys.append(templine[1])
            except:
                keys.append(None)
    for i in range(0,len(title)):
        listEvent.append(voiceEvent(title[i],keys[i],False))
    idx = 0
    while x:
        try:
            listEvent[idx].trigger()
            idx += 1
            if idx >= len(listEvent):
                idx = 0
        except:
            pass

def clearHotKey():
    fileName = os.path.join("Data","Settings","keybind.txt")
    title = []
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            title.append(templine[0])
    with open(fileName,'w') as wf:
        for j in range(0,len(title)):
            tempWord = title[j] + " " + " " + " " + " " + "\n"
            wf.write(tempWord)

def clearAll():
    fileName = os.path.join("Data","Settings","keybind.txt")
    with open(fileName,'w') as wf:
        wf.write(" ")
    dir_path = os.path.join("Data","HotkeyEvents")
    for path in os.listdir(dir_path):
            file_path = os.path.join(dir_path,path)
            os.remove(file_path)
    hotkeyFrame_Listbox.delete(0,tk.END)

#=======MAIN WINDOW SETUP

window = tk.Tk()
window.geometry("600x500")
window.title("Game Macro Entertainment(GME)")
window.resizable(False,False)
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.config(background="white")

iconFilePath = os.path.join("Assets","venus.png")
icon = tk.PhotoImage(file=iconFilePath)
window.iconphoto(True,icon)

img = myImage("file",30,30)
hotkeyimg = myImage("keyboard",30,30)
playimg = myImage("play",30,30)
stopimg = myImage("stop",30,30)
spotifyimg = myImage("spotify",30,30)
leagueimg = myImage("league",60,60)



#======OTHER WINDOWS
mainFrame = tk.Frame(window, width=600, height=500)
hotkeyFrame = tk.Frame(window, width=600, height=500)
changekeyFrame = tk.Frame(window, width=600, height=500)
bufferFrame = tk.Frame(window, width=600, height=500)

for frame in(mainFrame,hotkeyFrame,changekeyFrame,bufferFrame):
    frame.grid(row=0,column=0,sticky="news")



#======MAIN FRAME

mainFrame.config(background="white")

mainFrame_Label = tk.Label(mainFrame,text="Game Macro",
                    font=('Arial',40,'bold'),
                    bg='white').grid(row=0, column=5, padx= 150, pady= 0)

mainFrame_FileButton = tk.Button(mainFrame,
                    text = "Add File",
                    command=openFile,
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    image=img,
                    compound="left",
                    padx=5)

mainFrame_HotkeyButton = tk.Button(mainFrame,
                    text = "HotKeys",
                    command=lambda:showFrame(hotkeyFrame),
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    image=hotkeyimg,
                    compound="left",
                    padx=5)

mainFrame_StartButton = tk.Button(mainFrame,
                    text = "Play",
                    command=play,
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    image=playimg,
                    compound="left",
                    padx=5)

mainFrame_SpotifyButton = tk.Button(mainFrame,
                    text = "With Spotify",
                    command=sub,
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    image=spotifyimg,
                    compound="left",
                    padx=5)
                    
mainFrame_FileButton.grid(row=1, column=5, padx= 150, pady= 10)
mainFrame_HotkeyButton.grid(row=2, column=5, padx= 150, pady= 10)
mainFrame_StartButton.grid(row=3, column=5, padx= 150, pady= 10)
mainFrame_SpotifyButton.grid(row=4, column=5, padx= 150, pady= 10)

#=======HOTKEY FRAME

hotkeyFrame_WIDTH = 6
hotkeyFrame.config(background="white")

hotkeyFrame_Label = tk.Label(hotkeyFrame,
                    text="Keybinds:",
                    font=('Arial',20,'bold'),
                    bg='white')

count = 0
dir_path = os.path.join("Data","HotkeyEvents")
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

hotkeyFrame_Listbox = tk.Listbox(hotkeyFrame,bg="grey",
                        font=("Constantia",15),
                        width=12,
                        fg="white")
count = 0
for line in onlyfiles:
    hotkeyFrame_Listbox.insert(1,line)

hotkeyFrame_OptionButton = tk.Button(hotkeyFrame,
                text = "Options",
                command=lambda:getFileList(changekeyFrame),
                font=("Arial",15),
                fg="white",
                bg="grey",
                activeforeground="white",
                activebackground="grey",
                state=tk.ACTIVE,
                padx=5,
                )

filename = os.path.join("Data","Settings","keybind.txt")
title = []
keys = []
serial = []
with open(filename,'r',encoding="utf-8") as rf:
    for line in rf:
        line = line.strip()
        templine = line.split(" ")
        title.append(templine[0])
        try:
            keys.append(templine[1])
            serial.append(templine[2])
        except:
            keys.append(None)
            serial.append(None)
with open(filename,'w') as wf:
    for line in onlyfiles:
        cnt = 0
        for i in range(0,len(title)):
            if(line == title[i]):
                if keys[i] == None:
                    tempWord = title[i] + " " + " " + " " + "\n"
                else:
                    tempWord = title[i] + " " + keys[i] + " " + serial[i] + "\n"
                wf.write(tempWord)
                cnt = 1
        if(cnt == 0):
            tempWord = line + " " + "\n"
            wf.write(tempWord)
title = []
keys = []
serial = []
with open(filename,'r',encoding="utf-8") as rf:
    for line in rf:
        line = line.strip()
        templine = line.split(" ")
        
        title.append(templine[0])
        try:
            keys.append(templine[1])
            serial.append(templine[2])
        except:
            keys.append(None)
            serial.append(None)

hotkeyFrame_Display = tk.Label(hotkeyFrame,
                    text="Options:",
                    font=('Arial',20,'bold'),
                    bg='white')

hotkeyFrame_BackButton = tk.Button(hotkeyFrame,
                            text = "Back",
                            command=lambda:showFrame(mainFrame),
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5,
                            width=hotkeyFrame_WIDTH+2)

hotkeyFrame_ClearButton = tk.Button(hotkeyFrame,
                            text = "Clear Keys",
                            command=clearHotKey,
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5,
                            )

hotkeyFrame_ClearAllButton = tk.Button(hotkeyFrame,
                            text = "Clear All",
                            command=clearAll,
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5,
                            width=hotkeyFrame_WIDTH+2)

hotkeyFrame_Label.grid(row=0, column=1,padx=45,pady=0)
hotkeyFrame_Listbox.grid(row=1, column=1,padx=45,pady=0)
hotkeyFrame_Display.grid(row=2, column=1,padx=45,pady=0)
hotkeyFrame_OptionButton.grid(row=3, column=2,padx=0,pady=10)
hotkeyFrame_BackButton.grid(row=3, column=0,padx=45,pady=10)
hotkeyFrame_ClearButton.grid(row=4, column=2,padx=0,pady=10)
hotkeyFrame_ClearAllButton.grid(row=4, column=0,padx=45,pady=10)
hotkeyFrame_Listbox.config()

#=======HOTKEY CHANGE
titleString = StringVar()
keyString = StringVar()
serialString = StringVar()

changekeyFrame.config(background="white")
changekeyFrame_Label = tk.Label(changekeyFrame,
                    text="Current Configuration:",
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_Title = tk.Label(changekeyFrame,
                    textvariable=titleString,
                    font=('Arial',15,'bold'),
                    bg='white') 
changekeyFrame_KeyLabel = tk.Label(changekeyFrame,
                    text="Keybind:",
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_KeyName = tk.Label(changekeyFrame,
                    textvariable=keyString,
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_KeyEntry = tk.Entry(changekeyFrame,font=("arial",15),width=2)
changekeyFrame_KeyButton = tk.Button(changekeyFrame,
                            text = "Key Change",
                            command=keyChange,
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5)
changekeyFrame_SerialLabel = tk.Label(changekeyFrame,
                    text="Serial/Random:",
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_SerialDisplay = tk.Label(changekeyFrame,
                    textvariable=serialString,
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_SerialButton = tk.Button(changekeyFrame,
                            text = "Change:Random",
                            command=serialChange,
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5,
                            width=12)
changekeyFrame_GameLabel = tk.Label(changekeyFrame,
                    text="Game/Application:",
                    font=('Arial',15,'bold'),
                    bg='white')
changekeyFrame_GameDisplay = tk.Label(changekeyFrame,
                    image=leagueimg)
changekeyFrame_GameButton = tk.Button(changekeyFrame,
                            text = "Game Change",
                            command=sub,
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5)
changekeyFrame_BackButton = tk.Button(changekeyFrame,
                            text = "Back",
                            command=lambda:showFrame(hotkeyFrame),
                            font=("Arial",15),
                            fg="white",
                            bg="grey",
                            activeforeground="white",
                            activebackground="grey",
                            state=tk.ACTIVE,
                            padx=5)


changekeyFrame_Label.grid(row=0, column=1,padx=0)
changekeyFrame_Title.grid(row=1, column=1,padx=0)
changekeyFrame_KeyLabel.grid(row=2, column=1,padx=10,pady=40)
changekeyFrame_KeyName.grid(row=3, column=1,padx=10,pady=40)
changekeyFrame_KeyButton.grid(row=5, column=1,padx=10,pady=0)
changekeyFrame_KeyEntry.grid(row=4, column=1,padx=10,pady=40)
changekeyFrame_SerialLabel.grid(row=2, column=0,padx=10,pady=40)
changekeyFrame_SerialDisplay.grid(row=3, column=0,padx=10,pady=40)
changekeyFrame_SerialButton.grid(row=4, column=0,padx=10,pady=40)
changekeyFrame_GameLabel.grid(row=2, column=2,padx=10,pady=40)
changekeyFrame_GameDisplay.grid(row=3, column=2,padx=10,pady=40)
changekeyFrame_GameButton.grid(row=4, column=2,padx=10,pady=40)
changekeyFrame_BackButton.grid(row=5, column=0)

showFrame(mainFrame)

window.mainloop()
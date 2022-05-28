from asyncio.windows_events import NULL
from ntpath import join
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import csv
import os 
import pyautogui
import pydirectinput
import keyboard 
import random
import threading

pyautogui.PAUSE = 0.01
global x
x = False
def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\spong\\Documents\\Code\\projects\\macroGame",
                                            filetypes=(("Text Files","*.txt"),
                                            ("All Files","*.*")))
    newfilename = os.path.basename(filepath)
    newfilepath = os.path.join("Data",newfilename)
    with open(filepath,'r') as rf:
        with open(newfilepath,'w') as wf:
            for line in rf:
                wf.write(line)

def reset():
    pyautogui.keyUp('shift')


def trashEvent():
    fileName = os.path.join("Data","SionTrash.txt")
    with open(fileName,'r') as f:
        f_content = f.readlines()
        idx = random.randint(0,len(f_content)-1)
        pydirectinput.press('enter')
        pyautogui.write('/all ')
        pyautogui.keyDown('shift')
        pyautogui.write(f_content[idx])
        pyautogui.keyUp('shift')

def mainProgram():
    global x
    while x:
        try:
            if keyboard.is_pressed('9'):
                while(keyboard.is_pressed('9')):
                    pass
                trashEvent()
            reset()
        except:
            pass
def play():
    global x 
    if x:
        x = False
        startButton.config(text = "Play",
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
        startButton.config(text = "Stop",
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
def key():
    keyname = entrykey.get()
    print(keyname)

def hotkeyChange():
    hotkeyWindow = tk.Toplevel()
    hotkeyWindow.geometry("350x350")
    hotkeyWindow.config(background="white")

    label = tk.Label(hotkeyWindow,text="Current Key:",
                    font=('Arial',20,'bold'),
                    bg='white')
    label2 = tk.Label(hotkeyWindow,text="Press Any Key....",
                    font=('Arial',20,'bold'),
                    bg='white')
    global listbox
    print(listbox.get(listbox.curselection()))
    label.pack()
    label2.pack()
    global entrykey
    entrykey = tk.Entry(hotkeyWindow,font=("arial",15))
    buttonhotkey = tk.Button(hotkeyWindow,
                    text = "Change",
                    command=key,
                    font=("Arial",15),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    padx=5)
    entrykey.pack()
    buttonhotkey.pack()

def hotkey():
    newWindow = tk.Toplevel()
    newWindow.geometry("600x400")
    newWindow.config(background="white")
    count = 0
    dir_path = os.path.join("Data","HotkeyEvents")
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    global listbox
    listbox = tk.Listbox(newWindow,bg="grey",
                            font=("Constantia",15),
                            width=12,
                            fg="white")
    count = 0
    for line in onlyfiles:
        listbox.insert(1,line)
    optionButton = tk.Button(newWindow,
                    text = "Options",
                    command=hotkeyChange,
                    font=("Arial",15),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    padx=5)
    
    filename = os.path.join("Data","Settings","keybind.txt")
    title = []
    keys = []
    

    with open(filename,'r') as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            
            title.append(templine[0])
            try:
                keys.append(templine[1])
            except:
                keys.append(None)
    with open(filename,'w') as wf:
        for line in onlyfiles:
            cnt = 0
            for i in range(0,len(title)-1):
                if(line == title[i]):
                    if keys[i] == None:
                        tempWord = title[i] + " " + "\n"
                    else:
                        tempWord = title[i] + " " + keys[i] + "\n"
                    wf.write(tempWord)
                    cnt = 1
            if(cnt == 0):
                tempWord = line + " " + "\n"
                wf.write(tempWord)
    with open(filename,'r') as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            
            title.append(templine[0])
            try:
                keys.append(templine[1])
            except:
                keys.append(None)
    listbox.pack()
    optionButton.pack()
    listbox.config()

window = tk.Tk()
window.geometry("600x400")
window.title("Game Macro Entertainment(GME)")

iconFilePath = os.path.join("Assets","venus.png")
fileifconFilePath = os.path.join("Assets","file.png")
hotkeyFilePath = os.path.join("Assets","keyboard.png")
playFilePath = os.path.join("Assets","play.png")
stopFilePath = os.path.join("Assets","stop.png")
icon = tk.PhotoImage(file=iconFilePath)
window.iconphoto(True,icon)

fileimage = Image.open(fileifconFilePath)
resizeImage = fileimage.resize((30,30))
img = ImageTk.PhotoImage(resizeImage)

hotkeyimage = Image.open(hotkeyFilePath)
hotkeyImage = hotkeyimage.resize((30,30))
hotkeyimg = ImageTk.PhotoImage(hotkeyImage)

playimage = Image.open(playFilePath)
playImage = playimage.resize((30,30))
playimg = ImageTk.PhotoImage(playImage)

stopimage = Image.open(stopFilePath)
stopImage = stopimage.resize((30,30))
stopimg = ImageTk.PhotoImage(stopImage)

window.config(background="white")

label = tk.Label(window,text="Game Macro",
                    font=('Arial',40,'bold'),
                    bg='white').grid(row=0, column=5, padx= 150, pady= 0)


fileButton = tk.Button(window,
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
                    padx=5).grid(row=1, column=5, padx= 150, pady= 10)

hotkeyButton = tk.Button(window,
                    text = "HotKeys",
                    command=hotkey,
                    font=("Arial",30),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    image=hotkeyimg,
                    compound="left",
                    padx=5).grid(row=2, column=5, padx= 150, pady= 10)

startButton = tk.Button(window,
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

startButton.grid(row=3, column=5, padx= 150, pady= 10)
print("Threads Active:",threading.activeCount())
window.mainloop()
 
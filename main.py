import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import os 
import pyautogui
import pydirectinput
import keyboard 
import random
import threading
import spotipy
import lyricsgenius as lg

pyautogui.PAUSE = 0.01
global x
x = False

def cleanText():
    cnt = 0
    tempWord = ""
    fileNameRead = os.path.join("Data","Settings","OriginalTextSong.txt")
    fileNameWrite = os.path.join("Data","HotkeyEvents","Song.txt")
    fileBan = os.path.join("Data","Settings","banlist.txt")
    with open(fileBan,'r',encoding="utf-8") as ban:
        banLines = ban.readlines()
        for k in range(0,len(banLines)-1):
            banLines[k] = banLines[k].replace("\n","")
        with open(fileNameRead,'r',encoding="utf-8") as rf:
            with open(fileNameWrite,'w',encoding="utf-8") as wf:
                for line in rf:
                    cnt = 0
                    if line[0:1] == "\n":
                        cnt = 1
                    for i in range(0,len(line)):
                        if line[i] == "[":
                            cnt = 1
                    if cnt == 0:
                        templine = line.split(" ")
                        for word in templine:
                            word = word.replace("\n","")
                            if ''.join(char for char in word if char.isalnum()) in banLines:
                                temp = "*****"
                            else:
                                temp = word
                            tempWord = tempWord + " "+ temp
                        tempWord = tempWord + "\n"
                        wf.write(tempWord)
                        tempWord = ""

class voiceEvent:
    def __init__(self,text,key,serial):
        self.text = text
        self.key = key
        self.serial = serial
        self.idx = 0
    def trigger(self):
        global spotifyActive
        global oldSongTitle
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




def loginSpot(frame):
    client = loginFrame_ClientEntry.get()
    secret = loginFrame_SecretEntry.get()
    access = loginFrame_AccessEntry.get()
    fileName = os.path.join("Data","Settings","api.txt")
    with open(fileName,'w',encoding="utf-8") as wf:
        wf.write("ClientID: " + client + "\n")
        wf.write("SecretID: " + secret + "\n")
        wf.write("AccessToken: " + access + "\n")
    frame.tkraise()


def checkSpot(frame):
    global spotifyCounter
    global spotifyActive
    global oldSongTitle
    fileName = os.path.join("Data","Settings","api.txt")
    data = []
    cnt = True
    with open(fileName,'r',encoding="utf-8") as rf:
        for line in rf:
            line = line.strip()
            templine = line.split(" ")
            try:
                data.append(templine[1])
            except:
                frame.tkraise()
                cnt = False
    if data == []:
        frame.tkraise()
        cnt = False
    if cnt:
        if spotifyCounter:
            mainFrame_SpotifyButton.config(text="W/O Spotify",fg="red")
            spotifyCounter = False
            spotify_client_id = data[0]
            spotify_secret = data[1]
            spotify_redirect_url = 'http://google.com'

            scope = 'user-read-currently-playing'
            oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_url,
                                    scope=scope)
            token_dict = oauth_object.get_access_token()
            try:
                token = token_dict['access_token']
                fileName = os.path.join("Data","Settings","OriginalTextSong.txt")
                fileSong = os.path.join("Data","HotkeyEvents","Song.txt")
                with open(fileName,'w',encoding="utf-8") as wf:
                    wf.write(" ")
                with open(fileSong,'w',encoding="utf-8") as wf:
                    wf.write(" ")
                spotifyActive = True
            except:
                mainFrame_SpotifyButton.config(text="With Spotify",fg="white") 
                spotifyCounter = True
                spotifyActive= False

        else:
            mainFrame_SpotifyButton.config(text="With Spotify",fg="white") 
            spotifyCounter = True
            spotifyActive= False

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
            with open(newfilepath,'w',encoding="utf-8") as wf:
                for line in rf:
                    wf.write(line)
        hotkeyFrame_Listbox.insert(1,newfilename)
        os.remove(filepath)
        count = 0
        dir_path = os.path.join("Data","HotkeyEvents")
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        onlyfiles = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        count = 0
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
        with open(filename,'w',encoding="utf-8") as wf:
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
    with open(fileName,'w',encoding="utf-8") as wf:
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
    with open(fileName,'w',encoding="utf-8") as wf:
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
    global spotifyActive
    filename = os.path.join("Data","Settings","keybind.txt")
    listEvent = []
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
                if templine[2] == "Serial":
                    serial.append(True)
                else:
                    serial.append(False)
            except:
                keys.append(None)
                serial.append(None)
    for i in range(0,len(title)):
        listEvent.append(voiceEvent(title[i],keys[i],serial[i]))
    idx = 0
    if spotifyActive:
        fileName = os.path.join("Data","Settings","api.txt")
        data = []
        cnt = True
        with open(fileName,'r',encoding="utf-8") as rf:
            for line in rf:
                line = line.strip()
                templine = line.split(" ")
                try:
                    data.append(templine[1])
                except:
                    cnt = False
        if data == []:
            cnt = False
        if cnt:
            spotify_client_id = data[0]
            spotify_secret = data[1]
            spotify_redirect_url = 'http://google.com'
            genius_access_token = data[2]
            scope = 'user-read-currently-playing'
            oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_url,
                                    scope=scope)
            token_dict = oauth_object.get_access_token()
            try:
                token = token_dict['access_token']
                spotify_object = spotipy.Spotify(auth=token)
                genius_object = lg.Genius(genius_access_token)
                current = spotify_object.currently_playing()
                artist_name = current['item']['album']['artists'][0]['name']
                song_title = current['item']['name']
                oldSongTitle = song_title
                song = genius_object.search_song(title=song_title,artist=artist_name)
                lyrics = song.lyrics
                fileName = os.path.join("Data","Settings","OriginalTextSong.txt")
                with open(fileName,'w',encoding="utf-8") as wf:
                    wf.write(lyrics)
                cleanText()
            except:
                pass

    while x:
        try:
            listEvent[idx].trigger()
            idx += 1
            if idx >= len(listEvent):
                idx = 0
            if spotifyActive:
                current = spotify_object.currently_playing()
                song_title = current['item']['name']
                if oldSongTitle != song_title:
                    status = current['currently_playing_type']
                    if status == 'track':
                        oldSongTitle = song_title
                        artist_name = current['item']['album']['artists'][0]['name']
                        song = genius_object.search_song(title=song_title,artist=artist_name)
                        lyrics = song.lyrics
                        fileName = os.path.join("Data","songText.txt")
                        with open(fileName,'w',encoding="utf-8") as wf:
                            wf.write(lyrics)
                        cleanText()
            
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
    with open(fileName,'w',encoding="utf-8") as wf:
        for j in range(0,len(title)):
            tempWord = title[j] + " " + " " + " " + " " + "\n"
            wf.write(tempWord)

def clearAll():
    fileName = os.path.join("Data","Settings","keybind.txt")
    with open(fileName,'w',encoding="utf-8") as wf:
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
window.eval('tk::PlaceWindow . center')

iconFilePath = os.path.join("Assets","venus.png")
icon = tk.PhotoImage(file=iconFilePath)
window.iconphoto(True,icon)

img = myImage("file",30,30)
hotkeyimg = myImage("keyboard",30,30)
playimg = myImage("play",30,30)
stopimg = myImage("stop",30,30)
spotifyimg = myImage("spotify",30,30)
leagueimg = myImage("league",60,60)
geniusimgBig = myImage("genius",60,60)
spotifyimgBig = myImage("spotify",60,60)

#======OTHER WINDOWS
mainFrame = tk.Frame(window, width=600, height=500)
hotkeyFrame = tk.Frame(window, width=600, height=500)
changekeyFrame = tk.Frame(window, width=600, height=500)
bufferFrame = tk.Frame(window, width=600, height=500)
loginFrame = tk.Frame(window, width=600, height=500)

for frame in(mainFrame,hotkeyFrame,changekeyFrame,bufferFrame,loginFrame):
    frame.grid(row=0,column=0,sticky="news")

#======MAIN FRAME
global spotifyActive
global spotifyCounter
spotifyCounter = True
spotifyActive = False

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
                    command=lambda:checkSpot(loginFrame),
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

#=======LOGIN FRAME

loginFrame.config(background="white")

loginFrame_Label = tk.Label(loginFrame,text="Login For Spotify",
                    font=('Arial',20,'bold'),
                    bg='white')
loginFrame_ClientLabel = tk.Label(loginFrame,text="Spotify Client ID:",
                    font=('Arial',10,'bold'),
                    bg='white')
loginFrame_ClientEntry = tk.Entry(loginFrame,font=("arial",15),width=16)
loginFrame_ClientDisplay = tk.Label(loginFrame,
                    image=spotifyimgBig)
loginFrame_SecretLabel = tk.Label(loginFrame,text="Spotify Secret ID:",
                    font=('Arial',10,'bold'),
                    bg='white')
loginFrame_SecretEntry = tk.Entry(loginFrame,font=("arial",15),width=16)
loginFrame_SecretDisplay = tk.Label(loginFrame,
                    image=spotifyimgBig)
loginFrame_AccessLabel = tk.Label(loginFrame,text="Genius Access Token:",
                    font=('Arial',10,'bold'),
                    bg='white')
loginFrame_AccessEntry = tk.Entry(loginFrame,font=("arial",15),width=16)
loginFrame_AccessDisplay = tk.Label(loginFrame,
                    image=geniusimgBig)
loginFrame_Submit = tk.Button(loginFrame,
                    text = "Submit",
                    command=lambda:loginSpot(mainFrame),
                    font=("Arial",15),
                    fg="white",
                    bg="grey",
                    activeforeground="white",
                    activebackground="grey",
                    state=tk.ACTIVE,
                    padx=5)

loginFrame_Label.grid(row=0,column=1,padx=30,pady=0)
loginFrame_ClientLabel.grid(row=1,column=0,padx=10,pady=20)
loginFrame_ClientEntry.grid(row=1,column=1,padx=0,pady=20,columnspan=1)
loginFrame_ClientDisplay.grid(row=1,column=2,padx=20,pady=20)
loginFrame_SecretLabel.grid(row=2,column=0,padx=10,pady=20)
loginFrame_SecretEntry.grid(row=2,column=1,padx=0,pady=20,columnspan=1)
loginFrame_SecretDisplay.grid(row=2,column=2,padx=20,pady=20)
loginFrame_AccessLabel.grid(row=3,column=0,padx=10,pady=20)
loginFrame_AccessEntry.grid(row=3,column=1,padx=0,pady=20,columnspan=1)
loginFrame_AccessDisplay.grid(row=3,column=2,padx=20,pady=20)
loginFrame_Submit.grid(row=4,column=1,padx=0,pady=20)

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
with open(filename,'w',encoding="utf-8") as wf:
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
titleString = tk.StringVar()
keyString = tk.StringVar()
serialString = tk.StringVar()

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
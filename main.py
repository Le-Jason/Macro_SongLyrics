import pyautogui
import keyboard 
import os
import random
import spotipy
import lyricsgenius as lg

pyautogui.PAUSE = 0.1

def cleanText():
    cnt = 0
    tempWord = ""
    fileNameRead = os.path.join("Data","songText.txt")
    fileNameWrite = os.path.join("Data","cleansongText.txt")
    fileBan = os.path.join("Data","banlist.txt")
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
                

# spotify_client_id = 
# spotify_secret = 
# spotify_redirect_url = 'http://google.com'
# genius_access_token = 
scope = 'user-read-currently-playing'
oauth_object = spotipy.SpotifyOAuth(client_id=spotify_client_id,
                                    client_secret=spotify_secret,
                                    redirect_uri=spotify_redirect_url,
                                    scope=scope)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)
genius_object = lg.Genius(genius_access_token)
current = spotify_object.currently_playing()
artist_name = current['item']['album']['artists'][0]['name']
song_title = current['item']['name']
oldSongTitle = song_title
length = current['item']['duration_ms']
progress = current['progress_ms']
song = genius_object.search_song(title=song_title,artist=artist_name)
lyrics = song.lyrics
fileName = os.path.join("Data","songText.txt")
with open(fileName,'w',encoding="utf-8") as wf:
    wf.write(lyrics)
cleanText()
def sionEvent():
    fileName = os.path.join("Data","SionTalks.txt")
    with open(fileName,'r') as f:
        f_content = f.readlines()
        idx = random.randint(0,len(f_content)-1)
        pyautogui.press('enter')
        pyautogui.write('/all ')
        pyautogui.write(f_content[idx])
        pyautogui.press('enter')

def trashEvent():
    fileName = os.path.join("Data","SionTrash.txt")
    with open(fileName,'r') as f:
        f_content = f.readlines()
        idx = random.randint(0,len(f_content)-1)
        pyautogui.press('enter')
        pyautogui.write('/all ')
        pyautogui.keyDown('shift')
        pyautogui.write(f_content[idx])
        pyautogui.keyUp('shift')
        pyautogui.press('enter')

def luluEvent():
    fileName = os.path.join("Data","luluTalks.txt")
    with open(fileName,'r') as f:
        f_content = f.readlines()
        idx = random.randint(0,len(f_content)-1)
        pyautogui.press('enter')
        pyautogui.write('/all ')
        pyautogui.write(f_content[idx])
        pyautogui.press('enter')
def redfishEvent(idx):
    fileName = os.path.join("Data","RedFishBlueFish.txt")
    with open(fileName,'r') as f:
        f_content = f.readlines()
        pyautogui.press('enter')
        pyautogui.write('/all ')
        pyautogui.write(f_content[idx])
        pyautogui.press('enter')

def reset():
    pyautogui.keyUp('shift')

def readText(content):
    pyautogui.press('enter')
    pyautogui.write('/all ')
    pyautogui.write(content)
    pyautogui.press('enter')

def songEvent(idx):
    fileName = os.path.join("Data","cleansongText.txt")
    with open(fileName,'r',encoding="utf-8") as f:
        f_content = f.readlines()
        pyautogui.press('enter')
        pyautogui.write('/all ')
        pyautogui.write(f_content[idx])
        pyautogui.press('enter')


nextsongCNT = 0
fishidx = 0
songidx = 0
while True:
    try:
        if keyboard.is_pressed('-'):
            while(keyboard.is_pressed('-')):
                pass
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
                    songidx = 0
                    cleanText()
            songEvent(songidx)
            songidx = songidx + 1
        if keyboard.is_pressed('0'):
            while(keyboard.is_pressed('0')):
                pass
            sionEvent()
        if keyboard.is_pressed('9'):
            while(keyboard.is_pressed('9')):
                pass
            trashEvent()
        if keyboard.is_pressed('8'):
            while(keyboard.is_pressed('8')):
                pass
            redfishEvent(fishidx)
            fishidx = fishidx + 1
            if(fishidx>=200):
                fishidx = 0
        # reset()

    except:
        pass

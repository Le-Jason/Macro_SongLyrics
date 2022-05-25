import time
import pyautogui
import pydirectinput
import keyboard 
import os

pydirectinput.PAUSE = 0.001

global readLineIdx
readLineIdx = 0

def sionEvent():
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('me sion1 you peasant1 .;0')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

def karenEvent():
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('sorry this chat ai is toxic')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('i hope you have a nice day')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

def reset():
    pydirectinput.keyUp('shift')

def readText(content):
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.write(content)
    pydirectinput.press('enter')

def fixText(content):
    for i in range(0,len(content)-1):
        content[i] = content[i].lower()
    return content

cnt = 0
fileName = os.path.join("Data","RedFishBlueFish.txt")

while True:
    try:
        with open(fileName,'r') as f:
            if(cnt == 0):
                f_content = f.readlines()
                f_content = fixText(f_content)

                cnt = 1
            if keyboard.is_pressed('0'):
                while(keyboard.is_pressed('0')):
                    pass
                sionEvent()
            if keyboard.is_pressed('9'):
                while(keyboard.is_pressed('9')):
                    pass
                karenEvent()
            if keyboard.is_pressed('8'):
                while(keyboard.is_pressed('8')):
                    pass
                readText(f_content[readLineIdx])
                readLineIdx = readLineIdx + 1
                if(readLineIdx>=200):
                    readLineIdx = 0
            reset()
    except:
        pass

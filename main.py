import time
import pyautogui
import pydirectinput
import keyboard 
import os

pydirectinput.PAUSE = 0.001


global readLineIdx
readLineIdx = 0

def forestEvent():
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('run from the king1')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

def karenEvent():
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('its just a video game1')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('are you really mad at pixels/')
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')

def reset():
    pydirectinput.keyUp('shift')

def readText(content):
    

    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write(content)
    pydirectinput.keyUp('shift')
    pydirectinput.press('enter')


def fixText(content):
    for i in range(0,len(content)-1):
        content[i] = content[i].lower()
        print(content[i])

    return content
cnt = 0
fileName = os.path.join("Data","RedFishBlueFish.txt")

while True:
    try:
        with open(fileName,'r') as f:
            if(cnt == 0):
                f_content = f.readlines()
                f_content = fixText(f_content)
                print(f_content)
                cnt = 1
            if keyboard.is_pressed('0'):
                while(keyboard.is_pressed('0')):
                    pass
                forestEvent()
            if keyboard.is_pressed('9'):
                while(keyboard.is_pressed('9')):
                    pass
                karenEvent()
            if keyboard.is_pressed('8'):
                while(keyboard.is_pressed('8')):
                    pass
                readText(f_content[readLineIdx])
                readLineIdx = readLineIdx + 1
            reset()
    except:
        pass

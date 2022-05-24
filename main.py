import time
import pyautogui
import pydirectinput
import keyboard 
import os
import csv

pydirectinput.PAUSE = 0.01



def forestEvent():
    pydirectinput.press('enter')
    pydirectinput.write('/all ')
    pydirectinput.keyDown('shift')
    pydirectinput.write('run forest run1')
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

while True:
    if keyboard.is_pressed('ctrl+r'):
        while(keyboard.is_pressed('ctrl+r')):
            pass
        karenEvent()
    if keyboard.is_pressed('ctrl+t'):
        while(keyboard.is_pressed('ctrl+t')):
            pass
        karenEvent()

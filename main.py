import time
import pyautogui
import pydirectinput
import keyboard 
import os
import csv

pydirectinput.PAUSE = 0.01

while True:
    try:
        if keyboard.is_pressed('m') :
            while(keyboard.is_pressed('m')):
                pass
            pydirectinput.press('enter')
            pydirectinput.write('/all ')
            pydirectinput.write('salt')
            pydirectinput.press('enter')
    except:
        pass
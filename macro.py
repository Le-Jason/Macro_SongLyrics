import random
import pydirectinput
import pyautogui
import keyboard
import os

class voiceEvent:
    #Class that runs the marco events
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
    #Runs the random league \all events
        fileName = os.path.join("Data","HotkeyEvents",self.text)
        with open(fileName,'r',encoding="utf-8") as f:
            f_content = f.readlines()
            idx = random.randint(0,len(f_content)-1)
            pydirectinput.press('enter')
            pyautogui.write('/all ')
            pyautogui.write(f_content[idx])
    def serialLeagueEvent(self):
    #Runs the serial league \all events
        fileName = os.path.join("Data","HotkeyEvents",self.text)
        with open(fileName,'r',encoding="utf-8") as f:
            f_content = f.readlines()
            if self.idx >= len(f_content):
                self.idx = 0
            pydirectinput.press('enter')
            pyautogui.write('/all ')
            pyautogui.write(f_content[self.idx])

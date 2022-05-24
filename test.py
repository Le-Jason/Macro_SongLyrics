import pydirectinput
import keyboard 

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
    pydirectinput.write('its just a video game1 are you really mad at pixels/')

while True:
    try:
        if keyboard.is_pressed('ctrl+r'):
            while(keyboard.is_pressed('ctrl+r')):
                pass
            forestEvent()
        if keyboard.is_pressed('ctrl+k'):
            while(keyboard.is_pressed('ctrl+k')):
                pass
            karenEvent()
    except:
        pass

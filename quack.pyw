import sys
import subprocess
from threading import Thread

# Manually install all required packages, that do not come with python by default
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'keyboard'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'playsound'])

from keyboard import is_pressed
from playsound import playsound

characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

def worker(key: str, sound: str) -> None:
    while True:
        try:
            if is_pressed(key):
                playsound(sound, True)
        
        except:
            pass

if __name__ == '__main__':
    Thread(target=worker, args=['backspace', './sounds/whwhwh.mp3']).start()
    Thread(target=worker, args=['enter', './sounds/hihihihaw.mp3']).start()
    Thread(target=worker, args=['shift', './sounds/haha.mp3']).start()

    for char in characters:
        Thread(target=worker, args=[char, './sounds/quack.mp3']).start()
import pygame
import os
import sys
import time

audio = "assets/test/Giulio Cesare in Egitto, opera, HWV 17 (Public Domain).mp3"

def playAudio(filePath):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        position = pygame.mixer.music.get_pos() / 1000
        sys.stdout.write("\r|" + "#" * int(position) +
                         "-" * (100 - int(position)) + "|")

        sys.stdout.flush()
        time.sleep(0.1)

    pygame.mixer.music.stop()
    pygame.quit()


audioPath = audio.split('/')
audioFileName = audioPath[len(audioPath) - 1]

os.system('cls' if os.name == 'nt' else 'clear')

print(audioFileName)
playAudio(audio)

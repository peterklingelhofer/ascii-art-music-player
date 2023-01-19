import vlc
import time
import os

def playMusic(songPath):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(songPath)
    player.set_media(media)
    player.play()

    length = player.get_length() / 1000

    currentTime = 0

    while currentTime < length:
        currentTime = player.get_time() / 1000
        progress = currentTime / length

        os.system('cls' if os.name == 'nt' else 'clear')

        print('[' + '#' * int(progress * 20) + '-' * (20 - int(progress * 20)) + ']')

        time.sleep(0.5)

songPath = input("🎵 Enter the path of the song:")

playMusic(songPath)

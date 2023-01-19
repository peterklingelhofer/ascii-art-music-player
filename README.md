# ASCII Art Music Player
Play music and track song progress via ASCII art from the terminal.

A while loop is used to continuously get the current time of the song and calculate the progress, which is then displayed as ASCII art using the `#` character to represent the completed portion and the `-` character to represent the remaining portion of the song.

You can also adjust the number of `#` and `-` characters to change the resolution of the progress bar.

## Setup
```sh
git clone https://github.com/peterklingelhofer/ascii-art-music-player.git
cd ascii-art-music-player
python --version
pip install python-vlc
```

## Usage
```sh
python index.py
```

## Expected Test Output
```
Giulio Cesare in Egitto, opera, HWV 17 (Public Domain).mp3
|#################################################################-----------------------------------|
```
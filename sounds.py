from pygame import mixer

def click_SE():
    mixer.music.load('click1.wav')
    mixer.music.play(1)

def opt_background(on):
    mixer.music.load('background.mp3')
    mixer.music.play(-1)
    if on == False:
        mixer.music.stop()

def consume_SE():
    mixer.music.load('eat.wav')
    mixer.music.play(1)

def kill_SE():
    mixer.music.load('kill.wav')
    mixer.music.play(1)

def died_SE():
    mixer.music.load('kill.wav')
    mixer.music.play(1)


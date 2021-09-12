from tkinter import *
import pyttsx3

lyrics_edited = []

# reading text file with randomly generated lyrics
with open('Lyrics.txt', 'r') as rf:
    content = rf.read()
    content = content.split("\n")
    for line in content:
        if line != 'Verse 1' and line != 'Pre-Chorus' and line != 'Chorus' and line != 'Verse 2' and line != 'Bridge':
            lyrics_edited.append(line)

# computer reads contents
engine = pyttsx3.init()
engine.say(lyrics_edited)
engine.runAndWait()
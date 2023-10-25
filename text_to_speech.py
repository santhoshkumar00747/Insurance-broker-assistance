import subprocess
from gtts import gTTS

mytext = "Welcome to a to z insurance"
language = 'en'

myobj = gTTS(text=mytext, lang=language)

myobj.save("welcome.mp3")

subprocess.call(['mpg123',"welcome.mp3",'--play-and-exit'])


import requests
import speech_recognition as sr
import subprocess
from gtts import gTTS
 
bot_message = ""
message=""

while bot_message != "Bye" or bot_message != 'thanks':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said: {}".format(message))
        except:
            print("Couldn't recognize your voice")
    
    
    response = requests.post('http://localhost:5055/webhook', json={"message": message})
    if response.ok and response.json():  # Check if the response is successful and not empty
        responses = response.json()
        for i in responses:
            bot_message = i.get('text')
            if bot_message:
                print(f"{bot_message}")
                myobj = gTTS(text=bot_message, lang='en', slow=False)
                myobj.save("welcome.mp3")

                subprocess.call(['mpg123', "welcome.mp3", '--play-and-exit'])
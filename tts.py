from gtts import gTTS
tts = gTTS(text='you deserve the death penalty', lang='en')
tts.save("sound1.mp3")
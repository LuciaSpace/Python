from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("myText.mp3")

playsound("myText.mp3")

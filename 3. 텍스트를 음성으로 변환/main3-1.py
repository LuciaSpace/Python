from gtts import gTTS

text = "안녕하세요. 김정은입니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")

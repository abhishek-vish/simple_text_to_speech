import pyttsx3

text_speech = pyttsx3.init()
#text_speech.setProperty('rate',100)
voices  = text_speech.getProperty("voices")
# text_speech.setProperty('voices',voices[0])
# text_speech.setProperty('gender',voices.gender)
input_text = input("type something to convert into specch :")
text_speech.say(input_text)
text_speech.runAndWait()
text_speech.stop()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id[1])
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()
from googletrans import Translator
from gtts import gTTS
import os

def translate_func(en_text):
    # Creation an object - Translator
    translator = Translator()

    # Translating text from english to russian
    translated_text = translator.translate(en_text, src='en', dest='ru').text

    # Creating voice message on Russian
    tts = gTTS(text=translated_text, lang='ru', slow=False)

    # Saving voice message as .mp3 file near the .py file
    tts.save('Desktop/translated_voice_message.mp3')
    

# English text to translate
english_text = 'Hello, this is a test message to be translated into Russian and converted into a voice message.'

translate_func(english_text)
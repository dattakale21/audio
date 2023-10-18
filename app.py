# language_codes = {
#     "English": "en",
#     "Spanish": "es",
#     "French": "fr",
#     "Hindi": "hi",
#     "Marathi": "mr",
#     "Afrikaans": "af",
#     "Arabic": "ar",
#     "Armenian": "hy",
#     "Azerbaijani": "az",
#     "Belarusian": "be",
#     "Bosnian": "bs",
#     "Bulgarian": "bg",
#     "Catalan": "ca",
#     "Chinese": "zh",
#     "Croatian": "hr",
#     "Czech": "cs",
#     "Danish": "da",
#     "Dutch": "nl",
#     "Estonian": "et",
#     "Finnish": "fi",
#     "Galician": "gl",
#     "German": "de",
#     "Greek": "el",
#     "Hebrew": "he",
#     "Hungarian": "hu",
#     "Icelandic": "is",
#     "Indonesian": "id",
#     "Italian": "it",
#     "Japanese": "ja",
#     "Kannada": "kn",
#     "Kazakh": "kk",
#     "Korean": "ko",
#     "Latvian": "lv",
#     "Lithuanian": "lt",
#     "Macedonian": "mk",
#     "Malay": "ms",
#     "Maori": "mi",
#     "Nepali": "ne",
#     "Norwegian": "no",
#     "Persian": "fa",
#     "Polish": "pl",
#     "Portuguese": "pt",
#     "Romanian": "ro",
#     "Russian": "ru",
#     "Serbian": "sr",
#     "Slovak": "sk",
#     "Slovenian": "sl",
#     "Swahili": "sw",
#     "Swedish": "sv",
#     "Tagalog": "tl",
#     "Tamil": "ta",
#     "Thai": "th",
#     "Turkish": "tr",
#     "Ukrainian": "uk",
#     "Urdu": "ur",
#     "Vietnamese": "vi",
#     "Welsh": "cy",
# }

# def translate_audio():

#         # with open(filename, "rb") as audio:
#                     selected_language = input("Enter your language:")
#             # print(f"Selected Language: {selected_language}")

#                 # response = openai.Audio.transcribe("whisper-1", audio, lang="hi")


#                     # text_to_translate = response["text"]
#                     print(f"Selected Language: {selected_language}")
#                     target_language = language_codes[selected_language]
#                     print(f"Target Language: {target_language}")


#             # except openai.error.OpenAIError as e:
#             #     return f"OpenAI API error: {str(e)}"


# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator, constants
from googletrans import LANGUAGES
from werkzeug.utils import secure_filename
from gtts import gTTS
import os
import openai
import pyttsx3
import codecs
from pprint import pprint


language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Marathi": "mr",
    "Afrikaans": "af",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Belarusian": "be",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese": "zh",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "Estonian": "et",
    "Finnish": "fi",
    "Galician": "gl",
    "German": "de",
    "Greek": "el",
    "Hebrew": "he",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Macedonian": "mk",
    "Malay": "ms",
    "Maori": "mi",
    "Nepali": "ne",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog": "tl",
    "Tamil": "ta",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi",
    "Welsh": "cy",
}

print("hi")
def speakText():
    text = document.getElementsByName("transcribed_text")[0].value
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# print(translation.text)

# print(transcript)
# print(tt)
# from flask import Flask, render_template, request
# from langdetect import detect
# from googletrans import Translator, constants
# from googletrans import LANGUAGES
# from werkzeug.utils import secure_filename
# from gtts import gTTS
# import os
# import openai
# import codecs
# from pprint import pprint

# translator = Translator()
# translation = translator.translate("எத்தனை கவிங்கன் எழுதி பார்த்துக்கொண்டான் காதல் தீர்ந்து போகல எத்தனை னடிக்கன் நடிச்சு பார்த்துக்கொண்டான் காதல் போறே அடிக்கல எத்தனை காதல் உத்தங்கள் நடந்தும், காதல் தோல்க்காமல் இருக்கு எத்தனை கண்ணீர் சிந்தியும் காதல் ரொம்ப சுகமாய் இருக்கு இந்த காதல் இல்லையே, மனிதன் யாவரும் இருகமாக நேரும் ",dest='en')
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# if __name__ == '__main__':
#     audio_path = "audio3.mp3"  # Provide the path to your audio file
#     try:
#         result = transcribe_audio(audio_path)
#         print(result)
#     except Exception as e:
#         print(f"Error: {e}")

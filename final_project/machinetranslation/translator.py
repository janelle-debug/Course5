import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['Ve7ObnUQ3OmylLNZraiEU0RTHEwrYTAS5QVeHnMz8egQ']
url = os \
    .environ['https://api.us-south.language-translator.watson.cloud.ibm.com/instances/6d52c68d-5106-4028-8bb1-9026c7b4d95e']

def englishToFrench(englishText):
    englishText='My name is Janelle'
    french_translation= LanguageTranslatorV3.translate(text=englishText, model_id= 'en-fr') \
        .get_result()
    frenchText=french_translation
    return frenchText

def frenchToEnglish(frenchText):
    english_translation= LanguageTranslatorV3.translate(text=frenchText, model_id= 'fr-en').get_result()
    englishText=english_translation
    return englishText

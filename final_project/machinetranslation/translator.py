"""
Test Module doctsring
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """
    Function for translating English to French
    """
    french_text = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result().json
    return json.dumps(french_text, indent=2, ensure_ascii=False)

def french_to_english(french_text):
    """
    Function for translating French to English
    """
    english_text = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result().json
    return json.dumps(english_text, indent=2, ensure_ascii=False)

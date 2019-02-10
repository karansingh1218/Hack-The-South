import os
from google.cloud import translate
import json


def translate_language(text, google_application_credential_location):
    target_language = ['ru', 'chi', 'es']
    full_language_names = []
    
    for name in target_language:
        if name == 'ru':
            full_language_names.append('Russian')
        if name == 'chi':
            full_language_names.append('Chinese')
        if name == 'es':
            full_language_names.append('Spanish')
            
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_application_credential_location
    converted_language = []
    
	# Instantiates a client
    translate_client = translate.Client()
    
    for language in target_language:
        translate_value = translate_client.translate(text, target_language = language)
        mod_translate = translate_value['translatedText'] 
        converted_language.append(mod_translate)
        
    
    translation_dictionary = {full_language_names[0]: converted_language[0],
                              full_language_names[1]: converted_language[1],
                               full_language_names[2]: converted_language[2]}
    
    json_type_translation_dictionary = json.dumps(translation_dictionary)
    
    return json_type_translation_dictionary
from googletrans import Translator
from indic_transliteration.sanscript import transliterate, ITRANS, DEVANAGARI

def translate_text(choice, choice2, text):
    translator = Translator()

    lang_switch = {
        'French': 'fr',
        'English': 'en',
        'Spanish': 'es',
        'German': 'de',
        'Hindi': 'hi',
        'Italian': 'it',
        'Japanese': 'ja',
        'Chinese': 'zh-cn',
        'Russian': 'ru',
        'Arabic': 'ar',
        'Portuguese': 'pt',
        'Korean': 'ko',
        'Dutch': 'nl',
        'Turkish': 'tr',
        'Swedish': 'sv',
        'Polish': 'pl',
        'Greek': 'el',
        'Thai': 'th',
        'Vietnamese': 'vi',
        'Bengali': 'bn',
        'Urdu': 'ur',
        'Malay': 'ms',
        'Filipino': 'tl',
        'Czech': 'cs',
        'Hungarian': 'hu',
        'Finnish': 'fi',
        'Danish': 'da',
        'Norwegian': 'no',
        'Marathi': 'mr',
    }

    if choice == 'Hinglish':
        text = transliterate(text, ITRANS, DEVANAGARI)
        choice = 'Hindi'
    
    if choice == 'Mar-Eng':
        text = transliterate(text, ITRANS, DEVANAGARI)
        choice = 'Marathi'

    lang_from = lang_switch.get(choice)
    lang_to = lang_switch.get(choice2)

    if lang_to and lang_from:
        result = translator.translate(text, src=lang_from, dest=lang_to)
        return result.text
    else:
        raise ValueError("Invalid language choice.")
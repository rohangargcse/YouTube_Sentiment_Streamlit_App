
import re
import string
from deep_translator import GoogleTranslator

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return ' '.join([word for word in text.split() if len(word) > 2])

def clean_and_translate_comments(comments):
    cleaned = [clean_text(c) for c in comments]
    translations = []
    for c in comments:
        try:
            translated = GoogleTranslator(source='auto', target='en').translate(c)
            translations.append(translated)
        except:
            translations.append(c)
    return cleaned, translations

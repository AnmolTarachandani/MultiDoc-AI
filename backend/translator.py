from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer

def detect_language(text):
    return detect(text)

def translate_to_english(text, src_lang):
    if src_lang.startswith("en"):
        return text
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-en'
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
    except:
        return text  # Fallback
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
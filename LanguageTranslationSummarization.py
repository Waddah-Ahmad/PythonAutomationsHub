
# Project: Automated Language Translation and Summarization
"""
Description: This project automates the process of translating text from one language to another using a language translation API. 
It also summarizes the translated text to provide a concise overview.
"""

from google.cloud import translate_v2 as translate
from transformers import pipeline

def translate_text(text, target_language):
    client = translate.Client()
    translation = client.translate(text, target_language=target_language)
    translated_text = translation['translatedText']
    return translated_text

def summarize_text(text, max_length=100):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=max_length)[0]['summary_text']
    return summary

if __name__ == "__main__":
    # Ensure you have set up the Google Cloud Translation API and installed the required libraries.

    text_to_translate = "Enter the text you want to translate and summarize here."
    target_language = "fr"  # Replace with the target language code (e.g., "fr" for French)

    translated_text = translate_text(text_to_translate, target_language)
    summarized_text = summarize_text(translated_text)

    print("Original Text:")
    print(text_to_translate)
    print("\nTranslated Text:")
    print(translated_text)
    print("\nSummarized Text:")
    print(summarized_text)
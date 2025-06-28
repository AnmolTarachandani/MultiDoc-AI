# backend/summarizer.py

from transformers import pipeline
import torch

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    try:
        return summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    except:
        return "Could not summarize text."

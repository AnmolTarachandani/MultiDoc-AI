# backend/summarizer.py

from transformers import pipeline
import torch

# Load powerful summarization model
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    print("❌ Error loading summarizer model:", e)
    summarizer = None

def summarize_text(text):
    if not summarizer:
        return "Summarizer model not available."

    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("❌ Summarization failed:", e)
        return "Could not summarize text."


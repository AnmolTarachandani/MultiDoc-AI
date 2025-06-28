# backend/summarizer.py

from transformers import pipeline
import torch
import textwrap

# Choose device: CUDA if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)

def chunk_text(text, max_tokens=800):
    """
    Splits long text into chunks under a token limit (approx via word count).
    """
    words = text.split()
    for i in range(0, len(words), max_tokens):
        yield " ".join(words[i:i + max_tokens])

def summarize_text(text):
    """
    Summarizes large text by chunking and combining summaries.
    """
    try:
        if len(text.split()) < 30:
            return "⚠️ Text too short to summarize."

        summaries = []
        for chunk in chunk_text(text):
            summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # Combine chunked summaries into a final summary
        return "\n\n".join(textwrap.wrap(" ".join(summaries), width=120))

    except Exception as e:
        return f"❌ Could not summarize text. Error: {str(e)}"

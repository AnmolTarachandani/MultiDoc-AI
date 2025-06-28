from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    try:
        max_chunk_length = 700  # Safe chunk size (max for distilbart is 1024)
        sentences = text.split('. ')
        current_chunk = ''
        chunks = []

        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= max_chunk_length:
                current_chunk += sentence + '. '
            else:
                chunks.append(current_chunk.strip())
                current_chunk = sentence + '. '
        if current_chunk:
            chunks.append(current_chunk.strip())

        summarized_chunks = []
        for chunk in chunks:
            summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
            summarized_chunks.append(summary[0]['summary_text'])

        return ' '.join(summarized_chunks)

    except Exception as e:
        return f"❌ Could not summarize text. Error: {str(e)}"

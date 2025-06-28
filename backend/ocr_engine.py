from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
import io

def extract_text(file, ext):
    ext = ext.lower()
    
    if ext == ".pdf":
        try:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text
        except:
            return "❌ Could not read PDF content."

    elif ext == ".docx":
        try:
            doc = Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        except:
            return "❌ Could not read DOCX content."

    elif ext in [".png", ".jpg", ".jpeg"]:
        try:
            image = Image.open(file)
            return pytesseract.image_to_string(image)
        except:
            return "❌ Could not read image content."

    else:
        return "❌ Unsupported file type"

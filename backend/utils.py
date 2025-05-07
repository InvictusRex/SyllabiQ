import fitz  # PyMuPDF
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_from_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()

    if not text.strip():
        file.seek(0)
        images = convert_from_bytes(file.read())
        for img in images:
            text += pytesseract.image_to_string(img)

    return text
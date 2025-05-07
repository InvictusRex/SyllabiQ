import fitz  # PyMuPDF
from pdf2image import convert_from_bytes
import pytesseract

def extract_text_from_pdf(file, force_ocr=False):
    text = ""
    
    if force_ocr:
        # Convert PDF directly to images and process with OCR
        file.seek(0)
        images = convert_from_bytes(file.read())
        for img in images:
            text += pytesseract.image_to_string(img)
    else:
        # Try normal text extraction first
        pdf = fitz.open(stream=file.read(), filetype="pdf")
        for page in pdf:
            text += page.get_text()

        # Fallback to OCR if no text found
        if not text.strip():
            file.seek(0)
            images = convert_from_bytes(file.read())
            for img in images:
                text += pytesseract.image_to_string(img)

    return text.strip()
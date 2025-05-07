# SyllabiQ 📚

A smart tool for analyzing exam topic frequencies using Previous Year Questions (PYQ) and syllabus content.

## 🎯 Overview

SyllabiQ is an intelligent analyzer that helps students and educators understand which topics from a syllabus appear most frequently in previous year exam questions. Using Google's Gemini AI, it processes and classifies questions according to syllabus topics, helping in exam preparation and curriculum planning.

## ✨ Features

- 📄 PDF Processing for both syllabus and PYQ documents
- 🔍 Advanced OCR capabilities for scanned documents
- 🤖 Powered by Google's Gemini AI for intelligent analysis
- 📊 Topic frequency classification (Most frequent to least frequent)
- 🌐 User-friendly web interface
- 📱 Responsive design that works on both desktop and mobile

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/InvictusRex/SyllabiQ.git
cd SyllabiQ
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR:

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- **macOS:**
  ```bash
  brew install tesseract
  ```
- **Windows:**
  Download from [Tesseract GitHub Releases](https://github.com/UB-Mannheim/tesseract/wiki)

5. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🚀 Usage

1. Start the application:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Upload your files:

   - Select your syllabus PDF
   - Select your PYQ PDF

4. Wait for the analysis to complete
   - The tool will process both documents
   - Results will show topic-wise classification of questions

## 📂 Project Structure

```
SyllabiQ/
├── main.py              # Main Streamlit application
├── classifier.py        # Gemini AI integration
├── backend/
│   └── utils.py        # PDF processing utilities
├── requirements.txt     # Project dependencies
└── .env                # Environment variables (create this)
```

## 🔧 Technical Details

- **Frontend:** Streamlit
- **PDF Processing:** PyMuPDF, pdf2image
- **OCR Engine:** Tesseract (pytesseract)
- **AI Model:** Google Gemini
- **Language:** Python 3.x

## 📋 Requirements

- Python 3.x
- Tesseract OCR
- Google API Key for Gemini
- PDF processing libraries
- Streamlit

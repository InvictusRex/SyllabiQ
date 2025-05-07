import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def ask_gpt(messages):
    try:
        prompt = "\n".join([msg["content"] for msg in messages])

        # Initialize Gemini model inside function (v1 compatible)
        model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

        # Use generate_content for simple prompts
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "Error: Failed to get a response from Gemini."
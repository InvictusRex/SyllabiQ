import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

url = "https://fast.typegpt.net/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

def classify_questions_with_gpt(syllabus_topics, questions):
    prompt = (
        "You are a helpful assistant. You are given a list of topics from a syllabus and a list of exam questions.\n"
        "Your task is to categorize each question under the most relevant topic.\n"
        "Return a JSON dictionary with the topic as the key and a list of questions under that topic as the value.\n"
        "Here are the topics:\n"
        f"{syllabus_topics}\n\n"
        "Here are the questions:\n"
        f"{questions}\n"
    )

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error calling GPT API: {e}")
        return None

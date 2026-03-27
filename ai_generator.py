import requests
import json
import os

class AIContentGenerator:
    """
    Boilerplate for interacting with LLM APIs (OpenAI/Jasper) to generate marketing copy.
    """
    def __init__(self, api_key, engine="openai"):
        self.api_key = api_key
        self.engine = engine
        self.base_url = "https://api.openai.com/v1/chat/completions" if engine == "openai" else "https://api.jasper.ai/v1"

    def generate_copy(self, prompt, max_tokens=150):
        if self.engine == "openai":
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-4",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens
            }
            response = requests.post(self.base_url, headers=headers, json=payload)
            return response.json()['choices'][0]['message']['content']
        else:
            # Placeholder for Jasper API
            return "Generated Jasper Copy: " + prompt[:50]

if __name__ == "__main__":
    # Example usage
    # generator = AIContentGenerator(os.getenv("OPENAI_API_KEY"))
    # print(generator.generate_copy("Write a pin description for a wealth-building ebook."))
    print("AI Content Generator Boilerplate Ready.")

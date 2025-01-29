from openai import OpenAI

class TextGenerator:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, conversation_history):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        return response.choices[0].message.content

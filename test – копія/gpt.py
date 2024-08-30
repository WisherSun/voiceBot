from groq import Groq
client = Groq(api_key='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')

def generate(promt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': promt,
            }
        ],
        model='llama3-8b-8192',
    )
    return chat_completion.choices[0].message.content
# Simple AI Chat – no extra libraries needed except openai
# Comments in English

import os
from openai import OpenAI

# ====== SETTINGS ======
# Option 1: Use environment variable (recommended for GitHub)
# Mac/Linux: export OPENAI_API_KEY="sk-XXXX"
# Windows: setx OPENAI_API_KEY "sk-XXXX"
API_KEY = os.getenv("OPENAI_API_KEY")  # safer

# Option 2: Hardcode your key (only for personal testing)
# API_KEY = "sk-XXXX"

if not API_KEY:
    print("Warning: No API key found. Please set your OpenAI API key.")
    exit()

client = OpenAI(api_key=API_KEY)

print("AI chat is ready! Type 'exit' to quit.")

# ====== Chat history ======
chat_history = []

# ====== Chat loop ======
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Add user's message to history
    chat_history.append({"role": "user", "content": user_input})

    try:
        # Send all messages so far to AI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Answer clearly and concisely. If you don't know, say 'I don't know'. Do not make things up."}] + chat_history
        )

        ai_response = response.choices[0].message.content
        print("AI:", ai_response)

        # Add AI response to history
        chat_history.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print(f"Error connecting to AI: {e}")

# ====== Optional: save chat history to a file ======
try:
    with open("chat_history.txt", "w", encoding="utf-8") as f:
        for msg in chat_history:
            f.write(f'{msg["role"]}: {msg["content"]}\n')
    print("Chat history saved to chat_history.txt")
except Exception as e:
    print(f"Could not save chat history: {e}")
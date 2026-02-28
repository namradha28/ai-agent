import os
from dotenv import load_dotenv
from groq import Groq
from tools import calculate, get_weather, save_note, get_note

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🧠 Conversation memory
chat_history = [
    {"role": "system", "content": "You are an intelligent AI agent with memory."}
]


def run_llm(user_input):
    # Add user message to memory
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=chat_history,
        model="openai/gpt-oss-20b"
    )

    assistant_reply = response.choices[0].message.content

    # Add assistant reply to memory
    chat_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply


def run_agent(user_input):
    user_input_lower = user_input.lower()

    # 🔢 Math detection
    if any(op in user_input_lower for op in ["+", "-", "*", "/"]):
        return calculate(user_input)

    # 🌤 Weather
    if "weather" in user_input_lower:
        city = user_input.split()[-1]
        return get_weather(city)

    # 📝 Save note
    if user_input_lower.startswith("save"):
        try:
            _, key, value = user_input.split(maxsplit=2)
            return save_note(key, value)
        except:
            return "Format: save <key> <value>"

    # 📖 Get note
    if user_input_lower.startswith("get"):
        try:
            _, key = user_input.split(maxsplit=1)
            return get_note(key)
        except:
            return "Format: get <key>"

    # 🤖 Default → LLM with memory
    return run_llm(user_input)


if __name__ == "__main__":
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        print("Agent:", run_agent(user_input))
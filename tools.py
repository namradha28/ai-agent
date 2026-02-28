notes_db = {}

def calculate(expression: str):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

def get_weather(city: str):
    return f"The weather in {city} is 30°C and sunny."

def save_note(key: str, value: str):
    notes_db[key] = value
    return "Note saved successfully."

def get_note(key: str):
    return notes_db.get(key, "Note not found.")
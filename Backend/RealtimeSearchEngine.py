from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***"""

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=5))
    return results

def RealTimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    return data

def RealtimeSearchEngine(prompt):
    global System, messages

    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
    messages.append({"role": "user", "content": f"{prompt}"})

    results = GoogleSearch(prompt)
    answer = f"The search results for '{prompt}' are:\n"
    for result in results:
        answer += f"{result}\n"

    messages.append({"role": "assistant", "content": answer})
    with open(r"Data\ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    return answer

if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ")
        print(RealtimeSearchEngine(prompt))
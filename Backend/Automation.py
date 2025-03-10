import pyautogui
import webbrowser
import os

def automate_task(task):
    if task.startswith("open "):
        app_name = task.replace("open ", "")
        if app_name == "facebook":
            pyautogui.press("win")
            pyautogui.typewrite("facebook")
            pyautogui.press("enter")
        elif app_name == "telegram":
            pyautogui.press("win")
            pyautogui.typewrite("telegram")
            pyautogui.press("enter")
        elif app_name == "notepad":
            pyautogui.press("win")
            pyautogui.typewrite("notepad")
            pyautogui.press("enter")
        elif app_name == "google chrome":
            pyautogui.press("win")
            pyautogui.typewrite("google chrome")
            pyautogui.press("enter")
        elif app_name == "whatsapp":
            pyautogui.press("win")
            pyautogui.typewrite("whatsapp")
            pyautogui.press("enter")
        elif app_name == "instagram":
            pyautogui.press("win")
            pyautogui.typewrite("instagram")
            pyautogui.press("enter")
        elif app_name == "settings":
            pyautogui.press("win")
            pyautogui.typewrite("settings")
            pyautogui.press("enter")
        elif app_name == "omen gaming hub":
            pyautogui.press("win")
            pyautogui.typewrite("omen gaming hub")
            pyautogui.press("enter")
        elif app_name == "call of duty - infinite warfare":
            pyautogui.press("win")
            pyautogui.typewrite("call of duty - infinite warfare")
            pyautogui.press("enter")
    elif task.startswith("play "):
        song_name = task.replace("play ", "")
        if "on youtube" in song_name:
            song_name = song_name.replace(" on youtube", "")
            url = f"https://www.youtube.com/results?search_query={song_name}"
            webbrowser.open(url)
        elif "on spotify" in song_name:
            song_name = song_name.replace(" on spotify", "")
            url = f"https://open.spotify.com/search/{song_name}"
            webbrowser.open(url)
        elif "on apple music" in song_name:
            song_name = song_name.replace(" on apple music", "")
            url = f"https://www.apple.com/apple-music/search/{song_name}"
            webbrowser.open(url)
        else:
            url = f"https://www.youtube.com/results?search_query={song_name}"
            webbrowser.open(url)
    elif task.startswith("google search "):
        topic = task.replace("google search ", "")
        if "with keywords" in topic:
            topic, keywords = topic.split(" with keywords ")
            url = f"https://www.google.com/search?q={topic}+{keywords}"
        else:
            url = f"https://www.google.com/search?q={topic}"
        webbrowser.open(url)
    elif task.startswith("open youtube"):
        url = "https://www.youtube.com"
        webbrowser.open(url)
    elif task.startswith("mute"):
        pyautogui.press("volumemute")
    elif task.startswith("unmute"):
        pyautogui.press("volumemute")
    elif task.startswith("volume up"):
        pyautogui.press("volumeup")
    elif task.startswith("volume down"):
        pyautogui.press("volumedown")

if __name__ == "__main__":
    while True:
        task = input("Enter the task : ")
        if task.lower() == "exit":
            break
        automate_task(task)
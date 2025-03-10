import os
import mtranslate as mt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values(".env")

# Set input language from environment variable (default to English if not set)
InputLanguage = env_vars.get("InputLanguage", "en")

# HTML code for speech recognition
HtmlCode = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>Speech Recognition</title>
</head>
<body>
    <button id="start" onclick="startRecognition()">Start Recognition</button>
    <button id="end" onclick="stopRecognition()">Stop Recognition</button>
    <p id="output"></p>
    <script>
        const output = document.getElementById('output');
        let recognition;

        function startRecognition() {
            recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
            recognition.lang = '';
            recognition.continuous = true;

            recognition.onresult = function(event) {
                const transcript = event.results[event.results.length - 1][0].transcript;
                output.textContent += transcript;
            };

            recognition.onend = function() {
                recognition.start();
            };
            recognition.start();
        }

        function stopRecognition() {
            if (recognition) {
                recognition.stop();
            }
            output.innerHTML = "";
        }
    </script>
</body>
</html>
"""

# Replace language in HTML code with input language
HtmlCode = HtmlCode.replace("recognition.lang = '';", f"recognition.lang = '{InputLanguage}';")

# Create directory for Voice.html file if it doesn't exist
current_dir = os.getcwd()
voice_html_dir = os.path.join(current_dir, "Data")
os.makedirs(voice_html_dir, exist_ok=True)

# Write HTML code to Voice.html file
with open(os.path.join(voice_html_dir, "Voice.html"), "w", encoding="utf-8") as f:
    f.write(HtmlCode)

# Set up Chrome options
chrome_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-devices-for-media-stream")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless=new")

# Set up Chrome service
service = Service(ChromeDriverManager().install())

def SetAssistantStatus(Status):
    """Set the assistant status to the given status."""
    with open(os.path.join(current_dir, "Frontend", "Files", "Status.data"), "w", encoding="utf-8") as file:
        file.write(Status)

def SpeechRecognition():
    """Perform speech recognition using the Voice.html file."""
    try:
        # Initialize Chrome driver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to Voice.html file
        driver.get(f"file://{os.path.join(voice_html_dir, 'Voice.html')}")

        # Wait for start button to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "start")))

        # Click start button
        driver.find_element(By.ID, "start").click()

        while True:
            try:
                # Get text from output element
                Text = driver.find_element(By.ID, "output").text

                # If text is not empty, stop recognition and return text
                if Text:
                    driver.find_element(By.ID, "end").click()

                    # Translate text to English if input language is not English
                    if "en" not in InputLanguage.lower():
                        SetAssistantStatus("Translating...")
                        return mt.translate(Text, "en", "auto")
                    else:
                        return Text
            except Exception as e:
                print(f"Error during speech recognition: {e}")

    finally:
        # Quit Chrome driver
        driver.quit()

if __name__ == "__main__":
    while True:
        Text = SpeechRecognition()
        print(Text)
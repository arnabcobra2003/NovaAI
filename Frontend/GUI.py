import tkinter as tk
from Backend.Chatbot import ChatBot
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Model import FirstLayerDMM
from Backend.SpeechToText import SpeechRecognition

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot")

        self.input_field = tk.Text(self.window, height=10, width=40)
        self.input_field.pack()

        self.output_field = tk.Text(self.window, height=10, width=40)
        self.output_field.pack()

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        query = self.input_field.get("1.0", "end-1c")
        self.input_field.delete("1.0", "end")

        tasks = FirstLayerDMM(query)
        for task in tasks:
            if task.startswith("general"):
                query = task.replace("general ", "")
                answer = ChatBot(query)
            elif task.startswith("realtime"):
                query = task.replace("realtime ", "")
                answer = RealtimeSearchEngine(query)
            else:
                answer = task

            self.output_field.insert("end", "AI: " + answer + "\n")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChatbotGUI()
    gui.run()
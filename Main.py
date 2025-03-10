from Backend.Chatbot import ChatBot
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Model import FirstLayerDMM
from Backend.SpeechToText import SpeechRecognition

def main():
    while True:
        query = SpeechRecognition()
        print("User :", query)

        tasks = FirstLayerDMM(query)
        for task in tasks:
            if task.startswith("general"):
                query = task.replace("general ", "")
                print("AI:", ChatBot(query))
            elif task.startswith("realtime"):
                query = task.replace("realtime ", "")
                print("AI:", RealtimeSearchEngine(query))
            else:
                print("AI:", task)

if __name__ == "__main__":
    main()
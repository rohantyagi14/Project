import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
import pywhatkit as pw


# 🎤 Convert Speech to Text
def Speak_To_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        print("Silence please, calibrating background noise...")
        r.adjust_for_ambient_noise(source2, duration=2)
        print("Calibrated, now speak---")
        audio2 = r.listen(source2)

        try:
            print("Recognizing---")
            MyText = r.recognize_google(audio2, language="en-in")
            return MyText.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return "API unavailable"


# 🔊 Convert Text to Speech
def Text_to_speech(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice
    engine.setProperty('rate', 175)
    engine.say(command)
    engine.runAndWait()


# ✍️ Convert Text File to Handwriting Image
def Text_to_Handwriting():
    txt_path = "D:/Dummy.txt"  # your text file
    output_path = "D:/txt_to_hdw.png"

    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8") as f:
            text = f.read()

        pw.text_to_handwriting(text, output_path, [0, 0, 138])
        print(f"Handwriting image saved at {output_path}")
        Text_to_speech("Handwriting conversion completed successfully.")
    else:
        print("Text file not found.")
        Text_to_speech("Sorry, I could not find the text file.")


# 🚀 Main Program
if __name__ == '__main__':
    while True:
        data1 = Speak_To_Text()

        if not data1:
            continue

        if "your name" in data1:
            Text_to_speech("My name is Aakash Chaudhary")
        elif "old are you" in data1:
            Text_to_speech("I am 20 years old")
        elif "time" in data1:
            now = datetime.datetime.now().strftime("%I:%M %p")
            Text_to_speech(f"The time is {now}")
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "web" in data1:
            webbrowser.open("https://thecodingtracker.com/")
        elif "joke" in data1:
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            Text_to_speech(joke)
        elif "play song" in data1:
            music_folder = "D:/song"
            if os.path.exists(music_folder):
                songs = os.listdir(music_folder)
                if songs:
                    os.startfile(os.path.join(music_folder, songs[0]))
                    Text_to_speech("Playing your song now.")
                else:
                    Text_to_speech("No songs found in the folder.")
            else:
                Text_to_speech("Music folder not found.")
        elif "convert" in data1:
            Text_to_Handwriting()
        elif "exit" in data1:
            Text_to_speech("Thanks for visiting. Goodbye!")
            break

        time.sleep(2)

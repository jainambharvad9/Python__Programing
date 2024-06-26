import speech_recognition as sr
import webbrowser
import pyttsx3
import mcslib
recognizer = sr.Recognizer()
bharvad = pyttsx3.init()

def bol(text):
    bharvad.say(text)
    bharvad.runAndWait()
    
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")        
    elif"open github" in c.lower():
        webbrowser.open("https://github.com") 
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")   
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = mcslib.music[song]
        webbrowser.open(link)    
 
if __name__ == "__main__":
    bol("Initializing Alexander.....")  
    while True:
#         #listen for the weke word Alex
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                print("Recognizing.....")
                try:
                    word = r.recognize_google(audio)
                    print(f"Heard: {word}")
                    if (word.lower() == "alexander"):
                        bol("Yes")
                        print("Alexander Active....")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        processcommand(command)
                except sr.WaitTimeoutError:
                    print("Listening timed out, please try again.")
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
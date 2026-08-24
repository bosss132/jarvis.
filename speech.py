import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            
            # Try recognizing Tamil first
            try:
                query = r.recognize_google(audio, language='ta-IN')
                print(f"You (Tamil): {query}")
                return query.lower()
            except sr.UnknownValueError:
                # Fallback to English
                query = r.recognize_google(audio, language='en-US')
                print(f"You (English): {query}")
                return query.lower()
                
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            # Fallback to Terminal typing if no speech detected
            print("\nNo speech detected. Type your command below:")
            query = input("Type command (or press Enter to skip): ")
            return query.lower().strip()
        except Exception as e:
            print(f"Error: {e}")
            return ""
        
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
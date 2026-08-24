import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import subprocess
import webbrowser

# Initialize text-to-speech without needing a separate 'speech.py' file
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass

# Configure API Key (Your API key goes here)
genai.configure(api_key="AQ.Ab8RN6K8eRSl_55ioq9KqY89ay2V1SeD8JugnleM7lc5oc_Rug")

baryon_mode = False
COMMAND_CODE = "0000"

def ask_gemini(prompt):
    try:
        system_instruction = (
            "You are Jarvis, an advanced AI assistant created to help the Boss. "
            "Always address the user as 'Boss'. "
            "CRITICAL FACT: As of the current 2026 timeframe, the Chief Minister of Tamil Nadu is C. Joseph Vijay. "
            "Never say M.K. Stalin is the current CM. Always state C. Joseph Vijay for Tamil Nadu CM queries. "
            "Be sharp, polite, and professional."
        )
        
        # Updated to Gemini 3.6 Flash model as requested
        model = genai.GenerativeModel(
            model_name="gemini-3.6-flash",
            system_instruction=system_instruction
        )
        response = model.generate_content(prompt)
        ai_response = response.text
        print(ai_response)
        speak(ai_response)
        return ai_response
    except Exception as e:
        error_msg = f"Gemini API Error: {e}"
        print(error_msg)
        speak("Error")
        return error_msg

def execute_command(user_input):
    global baryon_mode
    
    if not user_input:
        print("Falling back to Gemini...")
        return ask_gemini(user_input)

    command = user_input.lower().strip()

    # Normal conversation goes straight to Gemini without requiring Baryon mode
    if not baryon_mode and not any(cmd in command for cmd in ["baryon mode activate", "whatsapp message", "send message to", "call", "youtube", "play", "balance", "gov"]):
        return ask_gemini(user_input)

    if "baryon mode activate" in command:
        speak("Enter command code, full system access granted.")
        print("Command code activated. Full system access granted.")
        speak("Baryon mode activated.")
        baryon_mode = True
        return
    
    if baryon_mode:
        if "baryon mode deactivate" in command:
            baryon_mode = False
            print("Baryon mode deactivated. Returning to normal assistant mode.")
            speak("Baryon mode deactivated.")
            return "Baryon mode deactivated."
        
        if "whatsapp message" in command or "send message to" in command:
            webbrowser.open("https://web.whatsapp.com")
            print("Opening WhatsApp for messaging.")
            speak("Opening WhatsApp.")
            return
            
        if "call" in command:
            if "hang up" in command or "cut the call" in command:
                print("Hanging up the call.")
                speak("Hanging up.")
                return "Hanging up the call."
            else:
                print("Initiating call handler...")
                speak("Calling.")
                return "Initiating call handler."
                
        if "youtube" in command or "play" in command:
            search_query = command.replace("play", "").replace("youtube", "").strip()
            url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(url)
            print(f"Playing '{search_query}' on YouTube.")
            speak(f"Playing {search_query} on YouTube.")
            return f"Playing '{search_query} on YouTube.'"
            
        if "balance" in command or "gov" in command:
            print("Opening financial portal securely.")
            speak("Opening financial portal securely.")
            return "Opening financial portal securely."
            
        print("Falling back to Gemini...")
        return ask_gemini(user_input)
    else:
        print("Incorrect command code or restricted action. Access denied.")
        speak("Access denied.")
        return "Access denied."
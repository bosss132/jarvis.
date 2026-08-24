import cv2
from modules.speech import speak, listen
from modules.commands import execute_command
from modules.commands import ask_gemini

def capture_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak("Cannot access camera.")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")
        speak("Photo captured successfully.")
    cap.release()


if __name__ == "__main__":
    speak("Jarvis initialized and ready.")

    while True:
        mode = input(
            "\nPress [Enter] to speak, or type your query directly: "
        ).strip()

        # Text input mode
        if mode:
            query = mode.lower()
        # Voice input mode
        else:
            query = listen()

        if not query:
            continue

        print(f"Query received: {query}")

        # Exit conditions
        if "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

        # Camera trigger
        elif (
            "camera" in query
            or "take photo" in query
            or "படம் எடு" in query
        ):
            capture_camera()

        # Other commands
        else:
         response = execute_command(query)
    if response:
        print(response)
        speak(ask_gemini(query))
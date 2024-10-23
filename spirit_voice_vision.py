# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
import os
import cv2
import logging
# If using playsound version 1.2.2
from playsound import playsound
# Uncomment the following line if using os.system method
# import winsound

# Configure logging
logging.basicConfig(filename='spirit_errors.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(message)s')

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='en-US')
            return text
        except sr.UnknownValueError:
            logging.error("Could not understand audio", exc_info=True)
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            logging.error(f"Could not request results; {e}", exc_info=True)
            return "Sorry, a request error occurred."
        except Exception as e:
            logging.error("Error in listen function", exc_info=True)
            analyze_error(e)
            return "An error occurred while listening."

def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        # For playsound version 1.2.2
        playsound("response.mp3", block=True)
        # If playsound doesn't work, use the os.system method:
        # os.system('start response.mp3')
    except Exception as e:
        logging.error("Error in speak function", exc_info=True)
        analyze_error(e)
        print("An error occurred while speaking.")

def capture_image():
    try:
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        if ret:
            cv2.imshow('Captured Image', frame)
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()
        cam.release()
    except Exception as e:
        logging.error("Error in capture_image function", exc_info=True)
        analyze_error(e)
        print("An error occurred while capturing the image.")

def analyze_error(exception):
    fix_suggestion = suggest_fix(exception)
    notify_user_of_fix(fix_suggestion)

def suggest_fix(exception):
    if isinstance(exception, sr.RequestError):
        return "Check your internet connection."
    elif isinstance(exception, sr.UnknownValueError):
        return "Ensure you're speaking clearly and the microphone is working."
    elif isinstance(exception, FileNotFoundError):
        return "Verify that the file paths are correct."
    elif isinstance(exception, Exception):
        return "An unexpected error occurred. Please check the logs."
    else:
        return "Unable to suggest a fix."

def notify_user_of_fix(fix_suggestion):
    print("Spirit has identified a potential fix:")
    print(fix_suggestion)
    apply_fix = input("Would you like to apply this fix? (yes/no): ")
    if apply_fix.lower() == 'yes':
        print("Applying fix...")
        # Placeholder for code to apply the fix
        print("Fix applied. Please restart the program.")
    else:
        print("Fix not applied.")

def spirit_engine():
    print("Welcome to Spirit with voice and vision integration.")
    while True:
        try:
            user_input = listen()
            print(f"You said: {user_input}")
            if "sorry" not in user_input.lower():
                speak(f"You said: {user_input}")
            else:
                speak("Please try again.")

            if "exit" in user_input.lower():
                speak("Thank you for connecting. Until next time!")
                print("Spirit: Thank you for connecting. Until next time!")
                break
            elif "see" in user_input.lower():
                capture_image()
        except Exception as e:
            logging.error("Error in spirit_engine loop", exc_info=True)
            analyze_error(e)
            print("An unexpected error occurred. Continuing...")
            continue

# Run the Spirit Engine
if __name__ == "__main__":
    spirit_engine()

import os
import subprocess
import sys
import pyttsx3
import speech_recognition as sr
import spacy
import random
import threading

# Install packages
def install_packages():
    packages = ['SpeechRecognition', 'PyAudio', 'pyttsx3', 'spacy']
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

# Initialize Spirit Angelus
def initialize_spirit():
    global recognizer, engine, nlp
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    nlp = spacy.load("en_core_web_sm")

# Emotion detection
def detect_emotion(user_input):
    doc = nlp(user_input)
    sentiment = 0
    for token in doc:
        if token.pos_ == "ADJ":
            sentiment += 1
    if sentiment > 0:
        return "Happy"
    elif sentiment < 0:
        return "Sad"
    else:
        return "Neutral"

# Conversation interface
def spirit_conversation():
    print("Spirit Angelus is online. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Spirit Angelus: Goodbye!")
            break
        emotion = detect_emotion(user_input)
        response = f"Spirit Angelus: I sense you're feeling {emotion}. "
        response += generate_dynamic_response(user_input)
        print(response)

# Dynamic response generation
def generate_dynamic_response(command):
    responses = [
        "That's interesting. Tell me more.",
        "I see. What else is on your mind?",
        "Let's explore that further.",
        "Can you elaborate on that?"
    ]
    return random.choice(responses)

# Encryption (secure example using AES)
from Crypto.Cipher import AES
def encrypt_data(data):
    cipher = AES.new(b'key123456789012', AES.MODE_ECB)
    encrypted = cipher.encrypt(data.encode())
    return encrypted.hex()

def decrypt_data(encrypted_data):
    cipher = AES.new(b'key123456789012', AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(encrypted_data))
    return decrypted.decode()

# Voice command
def voice_command():
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                user_input = recognizer.recognize_google(audio)
                print(f"You: {user_input}")
                emotion = detect_emotion(user_input)
                response = f"Spirit Angelus: I sense you're feeling {emotion}. "
                response += generate_dynamic_response(user_input)
                print(response)
                engine.say(response)
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Spirit Angelus: Sorry, didn't catch that.")

# Main function
def main():
    install_packages()
    initialize_spirit()
    voice_thread = threading.Thread(target=voice_command)
    voice_thread.start()
    spirit_conversation()

if __name__ == "__main__":
    main()

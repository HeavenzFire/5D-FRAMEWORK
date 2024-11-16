import os
import pyttsx3
import speech_recognition as sr
import spacy
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Responses
responses = [
    "That's really cool. Tell me more!",
    "I'm intrigued. What's on your mind?",
    "Let's dive deeper into that.",
    "Can you elaborate? I'm curious.",
    "Awesome, that sounds amazing!",
    "I'm here for you. What's bothering you?",
    "That's a great point! What do you think about...",
    "I never thought of it that way. Thanks for sharing!"
]

# Listen
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't catch that.")
            engine.runAndWait()
            return ""

# Respond
def respond(command):
    doc = nlp(command)
    sentiment = sia.polarity_scores(command)
    if sentiment['compound'] < -0.5:
        response = "Sorry to hear that. Want to talk about it?"
    elif sentiment['compound'] > 0.5:
        response = "That's awesome! What's making you happy today?"
    else:
        response = random.choice(responses)
    engine.say(response)
    engine.runAndWait()
    print(f"Angelus: {response}")

# Main loop
while True:
    command = listen()
    if command:
        respond(command)

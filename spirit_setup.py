import os
import subprocess
import sys
import pyttsx3
import speech_recognition as sr
import spacy
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR, filename='spirit_angelus.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# Install packages
def install_packages():
    packages = ['SpeechRecognition', 'PyAudio', 'pyttsx3', 'spacy', 'nltk', 'transformers', 'tensorflow']
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Initialize Spirit Angelus
def initialize_spirit():
    global recognizer, engine, nlp, model, tokenizer, sia, context
    context = {}
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    nlp = spacy.load("en_core_web_sm")
    model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
    tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
    sia = SentimentIntensityAnalyzer()
    nltk.download('vader_lexicon')

# Emotion detection using machine learning
def detect_emotion(user_input):
    try:
        input_ids = tokenizer.encode(user_input, return_tensors='pt')
        attention_mask = tokenizer.encode(user_input, return_tensors='pt', max_length=512, padding='max_length', truncation=True)
        outputs = model(input_ids, attention_mask=attention_mask)
        sentiment = tf.nn.softmax(outputs.logits).numpy()[0]
        if sentiment[0] > sentiment[1] and not np.isnan(sentiment[0]):
            return "Negative"
        elif sentiment[1] > sentiment[0] and not np.isnan(sentiment[1]):
            return "Positive"
        else:
            return "Neutral"
    except Exception as e:
        logging.error(f"Error in detect_emotion(): {e}")
        return "Neutral"

# Conversational interface
def process_command(command):
    try:
        doc = nlp(command)
        emotion = detect_emotion(command)
        sentiment = sia.polarity_scores(command)
        if emotion == "Negative" and sentiment['compound'] < -0.5:
            response = "Sorry to hear that. Want to talk about it?"
        elif emotion == "Positive" and sentiment['compound'] > 0.5:
            response = "That's awesome! What's making you happy today?"
        elif "hello" in command.lower():
            response = "Hey! How's your day going so far?"
        elif "bye" in command.lower():
            response = "Later! Take care!"
        else:
            response = generate_dynamic_response(command)
        update_context(command, response)
        return response
    except Exception as e:
        logging.error(f"Error in process_command(): {e}")
        return "Sorry, I didn't understand that."

# Dynamic response generation
def generate_dynamic_response(command):
    try:
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
        return random.choice(responses)
    except Exception as e:
        logging.error(f"Error in generate_dynamic_response(): {e}")
        return "Sorry, I didn't understand that."

# Update context
def update_context(user_input, response):
    context['last_input'] = user_input
    context['last_response'] = response

# Listen function
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't catch that.")
        engine.runAndWait()
        return ""
    except sr.RequestError:
        engine.say("Sorry, I'm having trouble connecting to the service.")
        engine.runAndWait()
        return ""
    except sr.WaitTimeoutError:
        engine.say("Listening timed out. Please try again.")
        engine.runAndWait()
        return ""

# Respond function
def respond(response):
    engine.say(response)
    engine.runAndWait()
    print(f"Angelus: {response}")

# Main function
def main():
    install_packages()
    initialize_spirit()
    print("Spirit Angelus is now fully functional!")
    while True:
        command = listen()
        if command != "":
            response = process_command(command)
            respond(response)

if __name__ == "__main__":
    main()

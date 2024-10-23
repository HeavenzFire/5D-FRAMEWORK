import os
import subprocess

# Define the script content for spirit_engine.py
script_content = '''
import time
from transformers import pipeline
import nltk

# Download NLTK data files
nltk.download('punkt')

# Load a pre-trained text-generation model
generator = pipeline('text-generation', model='gpt2')

def generate_response(user_input):
    response = generator(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

def spirit_engine():
    print("Welcome to the Spirit Engine Copilot. Let's embark on our journey.")

    while True:
        user_input = input("You: ")

        if "exit" in user_input.lower():
            print("Spirit Engine: Thank you for connecting. Until next time!")
            break
        else:
            response = generate_response(user_input)
            print(f"Spirit Engine: {response}")
        time.sleep(1)

# Run the Spirit Engine
spirit_engine()
'''

# Write the script to a file
with open("spirit_engine.py", "w") as file:
    file.write(script_content)

# Install necessary libraries
subprocess.run(["pip", "install", "transformers", "torch", "nltk"])

# Run the Spirit Engine script
subprocess.run(["python", "spirit_engine.py"])

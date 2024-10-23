import requests
from transformers import pipeline
import nltk

# Download NLTK data files
nltk.download('punkt')

# Load a pre-trained text-generation model
generator = pipeline('text-generation', model='gpt2', truncation=True, pad_token_id=50256)

# WebMD API endpoint (hypothetical example)
webmd_api_endpoint = "https://api.webmd.com/human-body-processes"

def get_webmd_info(query):
    response = requests.get(f"{webmd_api_endpoint}?query={query}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def generate_response(user_input):
    webmd_info = get_webmd_info(user_input)
    if webmd_info:
        response = f"According to WebMD, {webmd_info['summary']}."
    else:
        response = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
    return response

def spirit_engine():
    print("Welcome to Spirit with WebMD integration. How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if "exit" in user_input.lower():
            print("Spirit: Thank you for connecting. Until next time!")
            break
        else:
            response = generate_response(user_input)
            print(f"Spirit: {response}")

# Run the Spirit Engine
spirit_engine()

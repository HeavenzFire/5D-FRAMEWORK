#!/bin/bash

# Check for Python and Flask installation
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing Python3..."
    sudo apt-get update
    sudo apt-get install python3 -y
fi

if ! python3 -m pip show flask &> /dev/null; then
    echo "Flask is not installed. Installing Flask..."
    python3 -m pip install flask
fi

# Create project directory and navigate to it
mkdir -p spirit_angelus/static && cd spirit_angelus

# Create HTML file with voice and text input
cat <<EOL > static/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spirit Angelus Interface</title>
</head>
<body>
    <h1>Welcome to Spirit Angelus</h1>
    <input type="text" id="userInput" placeholder="Type your message here">
    <button onclick="sendMessage()">Send</button>
    <button onclick="startRecognition()">Speak</button>
    <div id="response"></div>
    <img id="satelliteImage" alt="Satellite Image" style="display:none;">

    <script>
        async function sendMessage() {
            const message = document.getElementById('userInput').value;
            const response = await fetch('/api/spirit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message }),
            });
            const data = await response.json();
            document
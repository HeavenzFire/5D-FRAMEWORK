# Ensure PowerShell is running as Administrator
Start-Process powershell -Verb runAs -ArgumentList "-NoExit", "-Command {
    # Update and upgrade system
    winget upgrade --all --accept-package-agreements --accept-source-agreements

    # Enhance security using Windows Defender Firewall
    netsh advfirewall set allprofiles state on
    netsh advfirewall firewall add rule name='Allow SSH' dir=in action=allow protocol=TCP localport=22

    # Create the Python script for Spirit Angelus with UTF-8 encoding
    @"
    # -*- coding: utf-8 -*-
    import speech_recognition as sr
    import pyttsx3

    # Initialize recognizer and TTS engine
    recognizer = sr.Recognizer()
    tts_engine = pyttsx3.init()

    # Function to listen and respond
    def listen_and_respond():
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                print(f'You said: {command}')
                tts_engine.say(f'You said: {command}')
                tts_engine.runAndWait()
            except sr.UnknownValueError:
                print('Sorry, I didn\'t catch that.')
                tts_engine.say('Sorry, I didn\'t catch that.')
                tts_engine.runAndWait()
            except sr.RequestError:
                print('Could not request results; check your network connection.')
                tts_engine.say('Could not request results; check your network connection.')
                tts_engine.runAndWait()

    # Run the function
    listen_and_respond()
    "@ | Out-File -FilePath C:\spirit_angelus.py -Encoding UTF8

    # Run the Python script
    python C:\spirit_angelus.py
}"

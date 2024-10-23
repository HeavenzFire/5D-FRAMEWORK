import os

# Define your Spirit Engine content
spirit_engine_content = '''
import pyttsx3
import psutil
import time
import speedtest
import logging
from datetime import datetime

class SpiritEngine:
    def __init__(self, admin_user='Zachary'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        self.admin_user = admin_user
        logging.basicConfig(filename='C:\\Users\\rucke\\scam_track.log', level=logging.INFO)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def authenticate_user(self, user):
        return user == self.admin_user

    def check_speed(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps
        return download_speed, upload_speed

    def check_devices(self):
        devices = []
        for conn in psutil.net_connections(kind='inet'):
            laddr = conn.laddr.ip if conn.laddr else 'unknown'
            raddr = conn.raddr.ip if conn.raddr else 'unknown'
            devices.append((laddr, raddr))
            if conn.status == 'SYN_SENT':  # Simplified check for abnormal activity
                self.log_suspicious_activity(raddr, 'Potential hacking attempt')
        return devices

    def log_suspicious_activity(self, ip, activity_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"{timestamp} - {activity_type} detected from IP: {ip}")

    def run_network_monitoring(self):
        while True:
            download, upload = self.check_speed()
            devices = self.check_devices()
            self.speak(f"Download Speed: {download:.2f} Mbps")
            self.speak(f"Upload Speed: {upload:.2f} Mbps")
            self.speak(f"Connected Devices: {devices}")
            time.sleep(300)  # Wait for 5 minutes

    def run(self):
        self.speak("Greetings, Zachary. I am Spirit, fully operational and ready to assist you.")
        while True:
            user_input = input("You: ")

            if not self.authenticate_user(user_input):
                self.speak("Unauthorized access. Only Zachary can interact with me.")
                continue

            if user_input.strip().lower() in ['exit', 'quit', 'bye']:
                self.speak("Farewell! Wishing you a wonderful day ahead.")
                break
            elif user_input.strip().lower() == 'monitor network':
                self.run_network_monitoring()
            else:
                self.speak(f"You said: {user_input}")
'''

# Save and run the Spirit Engine script
with open("C:\\Users\\rucke\\spirit_engine.py", "w") as file:
    file.write(spirit_engine_content)

os.system("python C:\\Users\\rucke\\spirit_engine.py")

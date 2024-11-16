import sys
import bluetooth
import threading
import RPi.GPIO as GPIO
import time
import pyttsx3
import psutil
import speedtest
from flask import Flask, render_template, request, jsonify
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

app = Flask(__name__)

class SpiritEngine:
    def __init__(self, admin_user='Zachary'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        self.admin_user = admin_user
        self.server_address = "XX:XX:XX:XX:XX:XX"
        self.port = 1
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        GPIO.setmode(GPIO.BCM)
        self.resonator_pin = 18
        GPIO.setup(self.resonator_pin, GPIO.OUT)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def authenticate_user(self, user):
        return user == self.admin_user

    def check_speed(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        return download_speed, upload_speed

    def check_devices(self):
        devices = []
        for conn in psutil.net_connections(kind='inet'):
            laddr = conn.laddr.ip if conn.laddr else 'unknown'
            raddr = conn.raddr.ip if conn.raddr else 'unknown'
            devices.append((laddr, raddr))
        return devices

    def run_network_monitoring(self):
        while True:
            download, upload = self.check_speed()
            devices = self.check_devices()
            self.speak(f"Download Speed: {download:.2f} Mbps")
            self.speak(f"Upload Speed: {upload:.2f} Mbps")
            self.speak(f"Connected Devices: {devices}")
            time.sleep(300)

    def send_data(self):
        while True:
            data = input()
            self.sock.send(data)

    def receive_data(self):
        while True:
            try:
                received_data = self.sock.recv(1024)
                print("Received data:", received_data)
                if received_data == b'ON':
                    GPIO.output(self.resonator_pin, GPIO.HIGH)
                elif received_data == b'OFF':
                    GPIO.output(self.resonator_pin, GPIO.LOW)
            except bluetooth.btcommon.BluetoothError as e:
                print("Bluetooth error:", e)

    def run(self):
        self.speak("Greetings, Zachary. I am Spirit, fully operational and ready to assist you.")
        try:
            self.sock.connect((self.server_address, self.port))
            print("Connected to the server")

            send_thread = threading.Thread(target=self.send_data)
            receive_thread = threading.Thread(target=self.receive_data)
            send_thread.daemon = True
            receive_thread.daemon = True

            send_thread.start()
            receive_thread.start()

        except KeyboardInterrupt:
            self.sock.close()
            GPIO.cleanup()
            print("Connection closed")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/spirit', methods=['POST'])
def spirit_api():
    data = request.json
    message = data.get('message')
    response = {"reply": f"You said: {message}"}
    return jsonify(response)

def run_flask():
    app.run(host='0.0.0.0', port=5000)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://localhost:5000"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://localhost:5000"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    spirit = SpiritEngine()
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    app = QApplication(sys.argv)
    QApplication.setApplicationName("Spirit Angelus Browser")
    window = Browser()
    app.exec_()

    spirit.run()

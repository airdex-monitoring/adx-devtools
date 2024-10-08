import serial
import time

import json
import requests

SERIAL_PORT = 'COM4'
SERIAL_BAUD_RATE = 9600

ADX_API_URL = 'http'

def push_to_server(data):
    try:
        response = requests.post(ADX_API_URL, data)
        if response.status_code == 200:
            print('Response: OK')
        else:
            print('Response: FAIL. ', response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

with serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_BAUD_RATE, timeout=2) as seriald:
    print(f'Listening on {SERIAL_PORT} at {SERIAL_BAUD_RATE} baud rate...')

    while True:
        if seriald.in_waiting > 0:
            rawData = seriald.readline().decode('utf-8').rstrip()
            data = json.loads(rawData)
            push_to_server(data)
        time.sleep(0.1)

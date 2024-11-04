import serial
import time

import json
import requests
import geocoder

SERIAL_PORT = 'COM4'
SERIAL_BAUD_RATE = 9600
ADX_API_URL = 'https://'
LOCATION_UPDATE_INTERVAL = 120

def push_to_server(data):
    try:
        response = requests.post(ADX_API_URL, json=data)
        if response.status_code == 200:
            print('Response: OK')
        else:
            print('Response: FAIL. ', response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

last_location_update_time = time.time()
location = geocoder.ip('me')

if location.ok:
    current_lat, current_lon = location.latlng

with serial.Serial(port=SERIAL_PORT, baudrate=SERIAL_BAUD_RATE, timeout=2) as seriald:
    print(f'Listening on {SERIAL_PORT} at {SERIAL_BAUD_RATE} baud rate...')

    while True:
        if seriald.in_waiting > 0:
            rawData = seriald.readline().decode('utf-8').rstrip()
            data = json.loads(rawData)

            current_time = time.time()
            if current_time - last_location_update_time >= LOCATION_UPDATE_INTERVAL:
                location = geocoder.ip('me')
                if location.ok:
                    current_lat, current_lon = location.latlng
                last_location_update_time = current_time
                print(f"Location updated at: {last_location_update_time.strftime('%Y-%m-%d %H:%M:%S')}")
            
            data['lat'] = current_lat
            data['lon'] = current_lon

            print(data)
            push_to_server(data)
        
        time.sleep(0.1)

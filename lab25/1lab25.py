import serial
import time

# Open serial port (change COM3 to your Arduino port)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

time.sleep(2)   # wait for Arduino to reset

def send_message(message):
    arduino.write((message + "\n").encode())   # send message to Arduino
    time.sleep(0.1)
    data = arduino.readline().decode().strip() # read Arduino response
    return data

# Send a sample message
msg = "Hello Arduino"
response = send_message(msg)

print("Message sent:", msg)
print("Arduino replied:", response)

arduino.close()

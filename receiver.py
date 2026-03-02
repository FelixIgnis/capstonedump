import serial
import time

# Configure the serial port
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1) # Or /dev/ttyAMA0

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            print("Received:", data.decode('utf-8'))
        time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()
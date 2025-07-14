import RPi.GPIO as GPIO
import time

BUTTON_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        print("Pressed!" if GPIO.input(BUTTON_PIN) else "Not pressed")
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
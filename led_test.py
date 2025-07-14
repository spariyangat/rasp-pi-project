import RPi.GPIO as GPIO
import time
print("here we go")

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO 16 as output
LED_pin = 4
GPIO.setup(LED_pin, GPIO.OUT)

# Turn LED on
GPIO.output(LED_pin, GPIO.HIGH)

# Keep it on for 10 seconds
time.sleep(10)

# Cleanup GPIO before exiting
GPIO.cleanup()
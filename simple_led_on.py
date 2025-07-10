import RPi.GPIO as GPIO
import time

print("Script started!")
GPIO.setmode(GPIO.BCM)

LED_PIN = 18
BUTTON_PIN = 4

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

GPIO.output(LED_PIN, GPIO.LOW) #making sure the LED starts off



try: 
    while True:
        if(GPIO.input(BUTTON_PIN) == GPIO.HIGH):
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)pyho
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


GPIO.cleanup()
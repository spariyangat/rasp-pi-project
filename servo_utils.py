
# Helper functions for servo, joystick, button, and LED testing/debugging

from gpiozero import Servo, MCP3008
from gpiozero.pins.pigpio import PiGPIOFactory
import RPi.GPIO as GPIO
from time import sleep
import math

factory = PiGPIOFactory()

servo_17 = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo_23 = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo_27 = Servo(27, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

vrx = MCP3008(channel=1)  # Horizontal axis
vry = MCP3008(channel=0)  # Vertical axis

GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

BUTTON_PIN = 12
GPIO.setup(BUTTON_PIN, GPIO.IN)

LED_PIN = 4
GPIO.setup(LED_PIN, GPIO.OUT)


# --- Helper Functions ---

def center_servo(servo=servo_17):
    # Center specified servo and hold
    print("Holding servo at mid position.")
    servo.mid()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Exiting center_servo.")


def cleanup_button_test():
    # Test button press detection and clean up GPIO
    try:
        while True:
            state = "Pressed!" if GPIO.input(BUTTON_PIN) else "Not pressed"
            print(state)
            sleep(0.2)
    except KeyboardInterrupt:
        print("Exiting cleanup_button_test.")
    finally:
        GPIO.cleanup()


def joystick_test():
    # Continuously print raw joystick values
    print("Starting joystick test...")
    try:
        while True:
            x = vrx.value  
            y = vry.value  
            print(f"Joystick X: {x:.2f}, Y: {y:.2f}")
            sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting joystick_test.")


def led_test(duration=10):
    # Turn LED on for specified duration in seconds, then cleanup
    print(f"Turning LED on pin {LED_PIN} on for {duration} seconds.")
    GPIO.output(LED_PIN, GPIO.HIGH)
    sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("LED test complete and GPIO cleaned up.")


def servo_six_test():
    # Cycle through servo min, max, mid positions on three servos
    print("Starting servo_six_test...")
    try:
        while True:
            servo_17.min()
            servo_27.min()
            sleep(0.1)
            servo_23.min()
            sleep(0.2)

            servo_17.max()
            sleep(0.05)
            servo_27.max()
            servo_23.max()
            sleep(0.2)

            servo_17.mid()
            servo_27.min()
            sleep(0.3)
            servo_23.mid()
            sleep(0.8)
            servo_17.max()
            sleep(0.4)
    except KeyboardInterrupt:
        print("Exiting servo_six_test.")

def button_led_test():
    print("Button-LED test started!")
    GPIO.setmode(GPIO.BCM)

    LED_PIN = 18
    BUTTON_PIN = 4

    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    GPIO.output(LED_PIN, GPIO.LOW)  # Start with LED off

    try: 
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
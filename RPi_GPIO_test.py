import RPi.GPIO as GPIO
import time

print("we have begun!")

GPIO.setmode(GPIO.BCM) #use broadcom pin numbering

servo_pin = 18 #set GPIO pin
LED_pin = 4
increase_button = 12
decrease_button = 21

GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(increase_button, GPIO.IN)
GPIO.setup(decrease_button, GPIO.IN)

pwm = GPIO.PWM(servo_pin, 50) #creates a PWM signal generator with 50Hz
pwm.start(0) #starts a 0% duty cycle (signal off)
#duty cycle is the percentage of one PWM period where the signal is HIGH (on)

GPIO.output(LED_pin, GPIO.LOW) #starts LED off

# Helper function to set angle (duty cycle)
def set_angle(angle):
    duty = 2 + (angle / 18)  #convert the angle (0–180 deg) to duty cycle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

# Helper function to keep the angle in the 0-180 degree range
def clamp_angle(angle):
    return max(0,min(180,angle))

try:
    angle = 90
    set_angle(angle)
    while True:
        if(GPIO.input(increase_button) == GPIO.HIGH):
            time.sleep(0.2)  # 200 ms delay to debounce
            angle += 10
            angle = clamp_angle(angle)
            set_angle(angle)
            GPIO.output(LED_pin, GPIO.HIGH)
        elif(GPIO.input(decrease_button) == GPIO.HIGH):
            time.sleep(0.2)  # 200 ms delay to debounce
            angle -= 10
            angle = clamp_angle(angle)
            set_angle(angle)
            GPIO.output(LED_pin, GPIO.HIGH)
        else:
            GPIO.output(LED_pin, GPIO.LOW)
        time.sleep(0.1)
    
finally: #so that the program always cleans up, even with an error in the try block
    pwm.stop()
    GPIO.cleanup()    


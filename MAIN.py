from gpiozero import Servo, MCP3008
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# --- SETUP ---

# Using the PiGPIO pin factory (a more precise hardware-based PWM backend) in order to reduce servo jitter
factory = PiGPIOFactory() 

# Set up the joystick vertical axis (connected to the MCP3008)
vry = MCP3008(channel=0) 

# Define left and right flap servos with calibrated pulse width ranges to ensure full rotation range 
right_flap = Servo(23, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory) 
left_flap = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)


# --- CONSTANTS ---
 
DEADZONE = 0.1                # Threshold below which joystick input is ignored
MAX_DEFLECTION_DEGREES = 60   # Maximum flap angle in degrees
RATE = 0.05                   # Rate at which the fla position changes 


# --- HELPER FUNCTIONS ---


def update_flaps(angle):
    # Update both flaps with symmetrical movement
    right_flap.value = angle
    left_flap.value = -angle # Invert for opposite direction

def set_flaps_to_neutral():
    # Set both flaps to neutral (0 degrees)
    global flap_position
    flap_position = 0
    update_flaps(flap_position)


# --- INITIALIZATION: ---

flap_position = 0      # Starting flap angle in servo units (-1 to 1)
prev_angle = None      # Previous angle in degrees
prev_neutral = None    # Previous deadzone state

set_flaps_to_neutral() # Making sure the flaps start off on neutral


# --- MAIN LOOP ---

try:
    while True:
        # Read and map joystick input (0 to 1) to servo range (-1 to 1)
        joystick_input = -1 * ((vry.value * 2) - 1)

        # Apply deadzone
        in_deadzone = abs(joystick_input) < DEADZONE
        if in_deadzone:
            joystick_input = 0

        # Update flap position incrementally
        flap_position += joystick_input * RATE 
        flap_position = max(-1, min(flap_position, 1)) # Clamp to valid servo range (-1 to 1)

        # Convert flap position to degrees and clamp to max physical deflection
        flap_angle = flap_position * 90
        flap_angle = max(-MAX_DEFLECTION_DEGREES, min(flap_angle, MAX_DEFLECTION_DEGREES))

        # Convert back to servo units to update hardware
        angle_servo_units = flap_angle / 90
        update_flaps(angle_servo_units)

        # Print flap angle only when it changes significantly
        if prev_angle is None or abs(flap_angle - prev_angle) > 4:
            print(f"Flap Angle Set To: {flap_angle:.1f}°")
            prev_angle = flap_angle

        # Print when entering/exiting neutral zone
        if prev_neutral is None or in_deadzone != prev_neutral:
            if in_deadzone:
                print("Joystick in neutral - holding flap position.")
            else:
                print("Joystick moved — updating flap position.")
            prev_neutral = in_deadzone

        sleep(0.05)

except KeyboardInterrupt:
    # Exiting program using Ctrl+C
    set_flaps_to_neutral()
    print("\nProgram exited by user...")

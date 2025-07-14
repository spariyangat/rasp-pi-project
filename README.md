# rasp-pi-project
Python code for experimenting with Raspberry Pi GPIO functionality

## Current Project: Servo Motor Control with Pushbuttons

This project uses a Raspberry Pi (Model 2 B) to control a servo motor with two pushbuttons to increment or decrement the angle. An LED turns on when the servo is active.

### Features
- Servo position control between 0° and 180°
- GPIO pushbutton input
- LED indicator
- Software-based PWM signal generation
- Button debouncing to prevent multiple unintended detections

### Issues Encountered
- **Servo jitter:** When powered directly from the Raspberry Pi's 5V rail, the servo motor is jittery and unreliable. This is due to insufficient current output from the Pi. Waiting on an external power supply from a servo kit.
- **Button bouncing:** Without debouncing, the button presses were sometimes detected multiple times. Added basic debouncing logic to improve reliability.
- **Breadboard power rail inconsistency:** Only one half of the breadboard's power rails seemed to work properly — discovered during troubleshooting an LED connection.
- **Old hardware:** Some components from the original 2014 starter kit (e.g., pushbuttons) were faulty and had to be replaced.



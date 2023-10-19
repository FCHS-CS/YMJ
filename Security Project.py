#remember to add status
import time
import board
import neopixel
import random
import digitalio as dio
import adafruit_hcsr04

#Mario defined the variables and inputs/outputs
num_pixels = 30
np = neopixel.NeoPixel(board.D2, num_pixels, auto_write = False, brightness = 1)

DISARMED = 0
ARMED = 1
ARMING = 2

pir = dio.DigitalInOut(board.D3)
pir.direction = dio.Direction.INPUT

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D5)

bb = dio.DigitalInOut(board.D6)
bb.direction = dio.Direction.INPUT
bb.pull = dio.Pull.UP

button = dio.DigitalInOut(board.D7)
button.direction = dio.Direction.INPUT
arm = button

button2 = dio.DigitalInOut(board.D8)
button2.direction = dio.Direction.INPUT
disarm = button2

red = (255, 0, 0)
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
purple = (255,0,255)
yellow = (255, 100, 0)
orangeT = (255, 80, 0)
orange = (255, 64, 0)
lightBlue = (87, 232, 255)
lightpurple = (227, 98, 255)
darkpurple = (18,0,18)
defaultcolor = [216, 231, 0]
status = DISARMED
#Mario defined the variables and inputs/outputs

#Yency did the Functions
'''
Function: fade_out

Description: This function begins with a color and fades to black

Parameters: defcolor(list), delay(float)

Return value: Prints the color values as they update
'''
def fade_out(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (defaultcolor[0] - (fadeR*i))
        color1[1] = int (defaultcolor[1] - (fadeG*i))
        color1[2] = int (defaultcolor[2] - (fadeB*i))
        np.fill(color1)
        print(i, defaultcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()

'''
Function: fade_in

Description: This function begins with a black and fades in to a color

Parameters: defcolor(list), delay(float)

Return value: Prints the color values as they update
'''
def fade_in(defaultcolor, delay = 0.005):
    fadeR = defaultcolor[0]/256.0
    fadeG = defaultcolor[1]/256.0
    fadeB = defaultcolor[2]/256.0
    for i in range(256):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        print(i, defaultcolor,fadeR*i,fadeG*i,fadeB*i)
        time.sleep(delay)
        np.show()

color1 = [defaultcolor[0],defaultcolor[1],defaultcolor[2]]
np.fill(color1)

'''
Function: disarmed

Description: This function changes the LED color to green to show the system is disarmed.


Return value: np.show()
'''
def disarmed():
    np.fill(green)
    np.show()
'''
Function: arming

Description: This function changes the LED color to yellow to show the system is arming.


Return value: np.show() & print(status)
'''
def arming():
    np.fill(yellow)
    np.show()
    status = ARMING
    print(status)
    time.sleep(10)
    '''
Function: armed

Description: This function changes the LED color to red to show the system is armed.


Return value: np.show()
'''
def armed():
    np.fill(red)
    np.show()
#Yency did the Functions

#Jaidyn created the base code, the entire group extened the code=
while True:
    if disarm.value != True:
        disarmed()
        status = DISARMED
        print(status)
        print(arm.value)

    if arm.value != True:
        arming()
        armed()
        status = ARMED
        print(status)

    if status == 1 and not bb.value:
        print("Beam is broken!, Triggering!")
        for i in range(30):
            fade_out(red)
            fade_in(red)
        armed()

    elif status == 1 and pir.value:
        print("Motion Detected, Triggering!")
        for i in range(10):
            fade_out(red)
            fade_in(red)
        armed()
        
    try:
        if status == 1 and sonar.distance <= 150:
            print("Triggered!")
            for i in range(10):
                fade_out(red)
                fade_in(red)
            armed()

    except RuntimeError:
        armed()
#Jaidyn created the base code, the entire group extened the code

import usb_hid
from digitalio import DigitalInOut, Pull,Direction
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from board import *

kbd = Keyboard(usb_hid.devices)

# LED
r_led = DigitalInOut(GP16)
r_led.direction = Direction.OUTPUT

g_led = DigitalInOut(GP17)
g_led.direction = Direction.OUTPUT

b_led = DigitalInOut(GP18)
b_led.direction = Direction.OUTPUT

y_led = DigitalInOut(GP19)
y_led.direction = Direction.OUTPUT

# button
r_tact = DigitalInOut(GP15)
r_tact.direction = Direction.INPUT
r_tact.pull = Pull.UP

g_tact = DigitalInOut(GP14)
g_tact.direction = Direction.INPUT
g_tact.pull = Pull.UP

b_tact = DigitalInOut(GP13)
b_tact.direction = Direction.INPUT
b_tact.pull = Pull.UP

y_tact = DigitalInOut(GP12)
y_tact.direction = Direction.INPUT
y_tact.pull = Pull.UP

while True:
    # Red Right
    if r_tact.value != 1:
        r_led.value = True
        kbd.press(Keycode.RIGHT_ARROW)
    else:
        r_led.value = False
        kbd.release(Keycode.RIGHT_ARROW)
    
    # Green Up
    if g_tact.value != 1:
        g_led.value = True
        kbd.press(Keycode.UP_ARROW)
    else:
        g_led.value = False
        kbd.release(Keycode.UP_ARROW)
        
    # Blue Down
    if b_tact.value != 1:
        b_led.value = True
        kbd.press(Keycode.DOWN_ARROW)
    else:
        b_led.value = False
        kbd.release(Keycode.DOWN_ARROW)
        
    # Yellow Left
    if y_tact.value != 1:
        y_led.value = True
        kbd.press(Keycode.LEFT_ARROW)
    else:
        y_led.value = False
        kbd.release(Keycode.LEFT_ARROW)
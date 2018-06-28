"""
Python 2.x

Program that flashes the Bright Pi camera LEDs when the Squid button is pressed.

Setup:
    - Bright Pi connected to 5, 6, 7 & 8
    - Squid button connected to 25 & 23
"""

from brightpi import *
import RPi.GPIO as GPIO
import time, os
from picamera import PiCamera

cam = PiCamera()
bps = BrightPiSpecialEffects()
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def flash():
    bps.reset()
    bps.beacon(1, 0.0025)
    num = len(os.listdir(DEST))
    cam.capture('{}/{}.jpg'.format(DEST, num))
    print str(num)+".jpg saved"
    bps.reset()
    
cam.start_preview()
while True:
    try:
        i = GPIO.input(25)
        if i == False:
            flash()
        time.sleep(0.2)
    except KeyboardInterrupt:
        cam.stop_preview()
        bps.reset()
        break

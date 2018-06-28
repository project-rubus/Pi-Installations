from brightpi import *
import RPi.GPIO as GPIO
import time

bps = BrightPiSpecialEffects()
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def flash():
    bps.reset()
    bps.beacon(1, 0.0025)
    bps.reset()
    
while True:
    i = GPIO.input(25)
    if i == False:
        flash()
    time.sleep(0.2)

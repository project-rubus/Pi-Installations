# Big Red Button (or the Squid Button)

See [here](https://github.com/simonmonk/squid)

## Interesting Websites

  * [https://github.com/simonmonk/squid](https://github.com/simonmonk/squid)
  * [https://www.monkmakes.com/squid-button/](https://www.monkmakes.com/squid-button/)
  
## Command I used:

  1. `git clone https://github.com/simonmonk/squid.git`
  2. `cd squid`
  3. `sudo python3 setup.py install`
  4. `pip3 install RPi.GPIO`
  
## Basic Script 
This only works when connected to pins 25 and the GND next to it

```python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP

while True:
    i = GPIO.input(25)
    if i == False:
        print("Button Pressed")
    time.sleep(0.2)
```

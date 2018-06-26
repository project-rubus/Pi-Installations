# Speaker pHAT

See [here](https://shop.pimoroni.com/products/speaker-phat)

## Interesting websites

  * [https://shop.pimoroni.com/products/speaker-phat](https://shop.pimoroni.com/products/speaker-phat)
  * [https://github.com/pimoroni/speaker-phat](https://github.com/pimoroni/speaker-phat)
  * [https://github.com/pimoroni/pivumeter](https://github.com/pimoroni/pivumeter)

## Commands I ran:
  1. `sudo apt-get install build-essential autoconf automake libtool libasound2-dev libfftw3-dev wiringpi`
  2. `git clone https://github.com/pimoroni/pivumeter`
  3. `cd pivumeter`
  4. `./setup.sh blinkt` -> This was not what I was meant to do, but I'm keeping it here for reference
  5. `./setup.sh speaker-phat`
 
## What I have to do:
  Somehow, I have to run `curl -sS https://get.pimoroni.com/speakerphat`, but it says `We can't connect to the Internet`. This is purely do to something being modified locally on the Pi. If `curl -sS https://get.pimoroni.com/speakerphat` is run, there shouldn't need to be a reason for the other steps.

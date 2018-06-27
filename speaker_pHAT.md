# Speaker pHAT

See [here](https://shop.pimoroni.com/products/speaker-phat). Unfortunately, the speaker itself does not work on a Raspian system, which is what is used by the Raspberry Pi I'm using. Only the 10 LEDs work.
## Interesting websites

  * [https://shop.pimoroni.com/products/speaker-phat](https://shop.pimoroni.com/products/speaker-phat)
  * [https://github.com/pimoroni/speaker-phat](https://github.com/pimoroni/speaker-phat)
  * [https://github.com/pimoroni/pivumeter](https://github.com/pimoroni/pivumeter)

## Method to install:
  1. `curl -sS https://get.pimoroni.com/speakerphat > script.sh`
  2. `nano script.sh`
  3. Replace 8.8.8.8 with www.ic.ac.uk
  4. `chmod 775 script.sh`
  5. `./script.sh`

## Commands I ran:
  1. `sudo apt-get install build-essential autoconf automake libtool libasound2-dev libfftw3-dev wiringpi`
  2. `git clone https://github.com/pimoroni/pivumeter`
  3. `cd pivumeter`
  4. `./setup.sh blinkt` -> This was not what I was meant to do, but I'm keeping it here for reference
  5. `./setup.sh speaker-phat`
  6. `curl -sS https://get.pimoroni.com/speakerphat > script.sh`
  7. `nano script.sh`
  8. Then I replaced 8.8.8.8 with www.ic.ac.uk
  9. `chmod 775 script.sh`
  10. `./script.sh`

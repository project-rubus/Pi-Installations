# Speaker pHAT

## Commands I ran:
  1. `sudo apt-get install build-essential autoconf automake libtool libasound2-dev libfftw3-dev wiringpi`
  2. `git clone https://github.com/pimoroni/pivumeter`
  3. `cd pivumeter`
  4. `./setup.sh blinkt` -> This was not what I was meant to do, but I'm keeping it here for reference
  5. `./setup.sh speaker-phat`
 
## What I have to do:
  Somehow, I have to run `curl -sS https://get.pimoroni.com/speakerphat`, but it says `We can't connect to the Internet`. I imagine the firewall doesn't like the `curl` command.
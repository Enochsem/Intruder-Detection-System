from hcsr04 import HCSR04
from machine import Pin
import time
import sys

pin = 21
pir = Pin(pin, Pin.IN, Pin.PULL_UP)
ledPin = 26
led = Pin(ledPin, Pin.OUT)

ultrasonic = HCSR04(trigger_pin=23, echo_pin=5)

delay = time.sleep_ms(300)

def distance():
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm')
    return distance

def main():
    while True:    
        pirState = pir.value()
        time.sleep_ms(200)
        if pirState == 1:
            print('Heat signature detected')
            if distance() <= 20:
                print("sending......")
                led.on()
                time.sleep(2)
        else:
            print('nothing')
            led.off()


try:
    main()
except KeyboardInterrupt:
    print('Ended')
    sys.exit()
    



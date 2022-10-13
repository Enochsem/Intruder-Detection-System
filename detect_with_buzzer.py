from hcsr04 import HCSR04
from machine import Pin, PWM
import time
import sys

pin = 21
pir = Pin(pin, Pin.IN, Pin.PULL_UP)

buzzerPin = Pin(33,Pin.OUT)
buzzer = PWM(buzzerPin)
buzzer.deinit()
buzzer.freq(2000)

def buzz():
    print("buzzing ...")
    buzzer.init()
    buzzer.duty(500)
    time.sleep(2)
    buzzer.duty(0)
    
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
                buzz()
                time.sleep(2)
        else:
            print('nothing')


try:
    main()
except KeyboardInterrupt:
    print('Ended')
    sys.exit()
    




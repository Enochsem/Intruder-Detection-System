#using the PIR SENSOR to detect call an interrupt and activate the system
#when motion is detected
from ultrasonic import *
from machine import Pin
import time
ledPin = 19
pirPin = 21
pir = Pin(pirPin, Pin.IN, Pin.PULL_UP)
led = Pin(ledPin, Pin.OUT)

detect = False

def pirCallBack(pin):
    global detect
    print(pin.value())
    if pin.value() == 1:
        detect = True
    
pir.irq(trigger=Pin.IRQ_RISING, handler=pirCallBack)
        
def main ():
    global detect
    if detect:  #if presence
        print("presence")
        distance = distance() #checkk distance
        print(distance)
        if distance <= 20: #if presence in range 20cm
            #do something
            led.on()
        else:
            detect = False
            




try:
    main()
except KeyboardInterrupt:
    print('Ended')
    
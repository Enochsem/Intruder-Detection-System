from machine import Pin, PWM
import time
buzzerPin = Pin(33,Pin.OUT)
buzzer = PWM(buzzerPin)
buzzer.deinit()
buzzer.freq(2000)

def buzz():
    print("buzzing ...")
    buzzer.init()
    buzzer.duty(512)
    time.sleep(2)
    buzzer.duty(0)
    
buzz()
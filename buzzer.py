from machine import Pin, PWM

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
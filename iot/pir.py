import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir = 18
led = 24

print('led on')
GPIO.setup(pir, GPIO.IN)
time.sleep(1)
GPIO.setup(led, GPIO.OUT)
print('led off')

GPIO.output(led, GPIO.HIGH)
time.sleep(1)
GPIO.output(led, GPIO.LOW)
time.sleep(1)

for i in range(15):
    if GPIO.input(pir):
        print('yay')
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        
GPIO.cleanup()

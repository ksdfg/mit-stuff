import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir = 18
led = 24

GPIO.output(led,GPIO.HIGH)

try:
    while(1):
        if GPIO.input(pir) != 1:
            GPIO.output(led, GPIO.HIGH)
        else:
            GPIO.output(led, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()

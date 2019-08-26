from gpiozero import MotionSensor, LED
from time import sleep

MotionSensor pir = MotionSensor(pin_no)
LED l = LED(pin_no)

def yes():
  l.on()
  sleep(0.5)
  l.off()

pir.when_motion = lambda: yes()

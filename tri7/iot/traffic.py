from gpiozero import TrafficLights
from time import sleep

lights = [
    TrafficLights(),
    TrafficLights(),
    TrafficLights(),
    TrafficLights()
]

lights[0].green.on()
lights[1].red.on()
lights[2].red.on()
lights[3].red.on()

for i in range(4):
    sleep(1)
    lights[i].amber.on()
    sleep(0.5)
    lights[i].red.on()
    lights[(i+1)%4].green.on()

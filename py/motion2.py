#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from gpiozero import MotionSensor
from gpiozero import LED
import time
LED_PIN = 4
MOTION_PIN = 15
if __name__ != '__main__':
    exit

print("start process")
ms = MotionSensor(MOTION_PIN)
led = LED(LED_PIN)
ms.wait_for_motion()
for i in range(10):
    if ms.motion_detected:
        led.on()
    else:
        led.off()
    time.sleep(1)
led.off()
print("end process")

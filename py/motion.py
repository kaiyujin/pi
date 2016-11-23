#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
LED_PIN = 4
MOTION_PIN = 15
if __name__ != '__main__':
    exit

print("start process")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(MOTION_PIN, GPIO.IN)
for i in range(1000):
    inputValue = GPIO.input(MOTION_PIN)
    print (inputValue)
    GPIO.output(LED_PIN, inputValue)
    time.sleep(0.1)
GPIO.cleanup()
print("end process")

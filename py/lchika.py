#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

if __name__ != '__main__':
    exit
    
ledFlag = False
ledNo = 2
interval=0.5

print("start process")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledNo, GPIO.OUT)

for i in range(10):
    GPIO.output(ledNo, ledFlag)
    time.sleep(interval)
    ledFlag = not(ledFlag)
GPIO.cleanup()
print("end process")

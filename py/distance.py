#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

LED_PIN = 4
TRIGER_PIN = 15
ECHO_PIN = 23
if __name__ != '__main__':
    exit

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(TRIGER_PIN, GPIO.IN)
GPIO.setup(TRIGER_PIN, GPIO.LOW)
GPIO.setup(ECHO_PIN, GPIO.IN)

GPIO.output(LED_PIN, True)
GPIO.output(TRIGER_PIN, True)
GPIO.output(TRIGER_PIN, False)

def execute(cnt):
    if cnt > 3:
        return "time out"
    try:
        startTime = time.time()
        while GPIO.input(ECHO_PIN) == 0:
            signaloff = time.time()
            if signaloff - startTime > 1:
                raise TimeoutError()
        while GPIO.input(ECHO_PIN) == 1:
            signalon = time.time()
            if signalon - startTime > 1:
                raise TimeoutError()
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        time.sleep(0.2)
        GPIO.output(LED_PIN, False)
        GPIO.cleanup()
        return distance
    except:
        cnt = cnt + 1
        execute(cnt)
    
print("start process")
print(execute(1))
print("end process")

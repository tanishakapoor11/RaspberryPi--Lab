import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
GPIO.output(19, GPIO.LOW)
time.sleep(1)
GPIO.output(19, GPIO.HIGH)
time.sleep(1)
GPIO.cleanup()

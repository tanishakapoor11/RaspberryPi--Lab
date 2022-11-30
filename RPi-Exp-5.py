import RPi.GPIO as GPIO
import time
# Led1 on my Board
led = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup( led, GPIO.OUT)
# 50Hz PWM Frequency
pwm_led = GPIO.PWM( led, 100)
# Full Brightness, 100% Duty Cycle
pwm_led.start(10)
try:
 while True:
 duty_s = raw_input("Enter Brightness Value (0 to 100):")
 duty = int(duty_s)
 pwm_led.ChangeDutyCycle(duty)
 time.sleep(1)
except KeyboardInterrupt:
 print ("Exiting Program")
except:
 print ("Error Occurs, Exiting Program")
finally:
 GPIO.cleanup()

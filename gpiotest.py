import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# 11	 13	    15
pin_num = 15
GPIO.setup(pin_num, GPIO.OUT)

#pin is now outputting LOW by default

GPIO.output(pin_num, GPIO.HIGH)
time.sleep(3)
GPIO.output(pin_num, GPIO.LOW)

# Clean up the GPIO settings
GPIO.cleanup()

import RPi.GPIO as GPIO
import time
# blinking function
def blink(pin, timer):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(timer)
        GPIO.output(pin,GPIO.LOW)

        return
def normalLED():
        # to use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BCM)
        # set up GPIO output channel
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        while True:
                blink(22,10)
                blink(27,3)
                blink(17,10)

        GPIO.cleanup()


import RPi.GPIO as GPIO
import time

# blinking function
def blink(pin, timer):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(timer)
        GPIO.output(pin,GPIO.LOW)

        return


def blinkemergence(pin1, pin2):

        while True:
                GPIO.output(pin1, GPIO.HIGH)
                GPIO.output(pin2, GPIO.HIGH)
        return

def normalLED():
        GPIO.cleanup()
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

def emergenceLED():
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        while True:
                blinkemergence(4 , 22)

        GPIO.cleanup()
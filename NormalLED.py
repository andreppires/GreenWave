import RPi.GPIO as GPIO
import time
import globaldict


def LEDS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    while True:
        if not globaldict.emergence:
            print "normal"
            for i in range(30):
                if globaldict.emergence:
                    GPIO.output(4, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.LOW)
                    break
                GPIO.output(27, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)

            for i in range(100):
                if globaldict.emergence:
                    GPIO.output(4, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.LOW)
                    break
                GPIO.output(17, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(22, GPIO.LOW)

            for i in range(100):
                if globaldict.emergence:
                    GPIO.output(4, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.LOW)
                    break
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                time.sleep(0.1)

        else:
            print "emergencia"
            GPIO.output(22, GPIO.HIGH)
            while True:
                if not globaldict.emergence:
                    GPIO.output(4, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.LOW)
                    break
                    GPIO.output(4, GPIO.HIGH)
                time.sleep(0.5)

                GPIO.output(4, GPIO.LOW)
                time.sleep(0.5)

import RPi.GPIO as GPIO
import time
import globaldict
GPIO.setmode(GPIO.BCM)

# blinking function
def blink(pin, timer):
    # to use Raspberry Pi board pin numbers


    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)
    if globaldict.emergence:
        GPIO.setup(22, GPIO.OUT)
        GPIO.output(22, GPIO.HIGH)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(timer)
    GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

    return


def normalLED():

    # to use Raspberry Pi board pin numbers
    # set up GPIO output channel
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(22, GPIO.LOW)
    flag=0
    while True:
        print "NORMAL LED"
        if globaldict.emergence:
            flag = 0
        if flag==0 :
            for i in range(100):
                blink(22, 0.1)
                print "VERDE"
                if globaldict.emergence:
                    GPIO.cleanup()
                    flag=1
                    break
        if not flag :
            for i in range(30):
                blink(27, 0.1)
                print "AMARELO"
                if globaldict.emergence:
                    GPIO.cleanup()
                    flag = 1

                    break
        if not flag:
            for i in range(100):
                blink(17, 0.1)
                print "VERMELHO"
                if globaldict.emergence:
                    GPIO.cleanup()
                    flag=1

                    break
    GPIO.cleanup()


def emergenceLED():
    print "emergenceLED0"
    while True:
        if globaldict.emergence == 1:

            GPIO.setup(4, GPIO.OUT)
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17, GPIO.LOW)
            GPIO.setup(27, GPIO.OUT)
            GPIO.output(27, GPIO.LOW)
            print "emergenceLED1"
            while True:
                print "emergenceLED2"
                blink(4,1)
                if globaldict.emergence != 1:
                    GPIO.output(22, GPIO.LOW)
                    GPIO.output(4, GPIO.LOW)
                    GPIO.cleanup()
                    break
            print "emergenceLED3"

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
                print "Amarelo"
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
                print "Vermelho"
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
                print "Verde"
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



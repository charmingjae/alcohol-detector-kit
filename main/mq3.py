import RPi.GPIO as GPIO
import time
from timerbot import poop
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

D0=26
LED1=19
LED2=13
PIEZO=6

GPIO.setmode(GPIO.BCM)
GPIO.setup(D0, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(PIEZO, GPIO.OUT)

updater = Updater("1422387923:AAH9-XFd06TtZ1yHm2TNRZeKchpwCKx7Xfs", use_context=True)

try:
    while True:
        if GPIO.input(D0) == False:
            print("Alcohol Level is high!")
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            GPIO.output(PIEZO, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(PIEZO, GPIO.LOW)
            poop()

        else:
            print("Alcohol Level is low.")
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()

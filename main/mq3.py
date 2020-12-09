# main process file

# import part
import RPi.GPIO as GPIO
import time
from timerbot import poop
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# define variable of object
D0 = 26
LED1 = 19
LED2 = 13
PIEZO = 6

# Setmode / Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(D0, GPIO.IN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(PIEZO, GPIO.OUT)

# define updater for telegram
updater = Updater(
    "1422387923:AAH9-XFd06TtZ1yHm2TNRZeKchpwCKx7Xfs", use_context=True)

# do try
try:
    # loop while keyboardinterrupted
    while True:
        # D0에 전류가 흐르지 않을 때
        if GPIO.input(D0) == False:
            print("Alcohol Level is high!")
            # LED 2개 점등
            GPIO.output(LED1, True)
            GPIO.output(LED2, True)
            # 부저 ON
            GPIO.output(PIEZO, GPIO.HIGH)
            time.sleep(1)
            # 부저 OFF
            GPIO.output(PIEZO, GPIO.LOW)
            # Call telegram function
            poop()
        # 전류가 흐를 때
        else:
            print("Alcohol Level is low.")
            # LED 끄기
            GPIO.output(LED1, False)
            GPIO.output(LED2, False)
        time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()

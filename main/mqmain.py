from timerbot import poop
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import time

updater = Updater(
    "1422387923:AAH9-XFd06TtZ1yHm2TNRZeKchpwCKx7Xfs", use_context=True)


def mqtest():
    while(True):
        for i in range(10):
            print('ing ...')
            time.sleep(1)
        print('Detected!!')
        poop()
        time.sleep(1)


if __name__ == '__main__':
    mqtest()

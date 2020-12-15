import time


def mqtest():
    while(True):
        for i in range(6):
            print('ing ...')
            time.sleep(1)
        print('Alcohol Detected!!')
        time.sleep(1)


if __name__ == '__main__':
    mqtest()

import os
import time


if __name__ == '__main__':
    while True:
        os.system('taskkill /F /IM hosts-server.exe')
        os.system('start /B hosts-server.exe')
        time.sleep(60*60)
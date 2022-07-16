import os
import time


if __name__ == '__main__':
    while True:
        os.system('taskkill /F /IM hosts-server.exe')
        os.system('start /B \"C:\\Users\\jiera\\Desktop\\新建文件夹\\hosts-server-pkg-win-x64\\hosts-server.exe\"')  # 必须引用绝对路径
        time.sleep(60*60)
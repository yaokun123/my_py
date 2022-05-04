# coding:utf-8

import os
import time

def choose():
    # 选菜
    os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 1000 940")
    time.sleep(2)
    # 确认
    os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 520 2274")


def up():
    os.popen(adb_path + " -s 6HJDU20214024902 shell input swipe 878 1280 729 943 400")
    time.sleep(2)

adb_path = "/usr/local/bin/adb"

# 1、关闭和启动adb服务
os.popen(adb_path + " kill-server")
os.popen(adb_path + " start-server")

# 2、检测连接设备列表
res = os.popen(adb_path + " devices")
print res.read()

# 打开电源键并解锁
os.popen(adb_path + " -s 6HJDU20214024902 shell input keyevent 26")
os.popen(adb_path + " -s 6HJDU20214024902 shell input swipe 350 1300 600 360 400")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 860 1415")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 860 1415")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 550 1635")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 550 1635")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 170 1200")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 170 1200")

# 打开美团
os.popen(adb_path + " -s 6HJDU20214024902 shell input swipe 900 809 350 800 400")
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 155 1500")
time.sleep(2)

# 选择美团买菜
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 350 734")
time.sleep(2)

# 选择素菜豆制品
os.popen(adb_path + " -s 6HJDU20214024902 shell input tap 116 1010")
time.sleep(2)

choose()
up()
up()

choose()
up()
up()

choose()

# choose()
# 3、
# while True:
#     os.popen(adb_path + " -s 6HJDU20214024902 shell input swipe 350 1300 600 500 400")
#     time.sleep(3)


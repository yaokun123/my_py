# coding:utf-8

import os
import time

adb_path = "/usr/local/bin/adb"

# 1、关闭和启动adb服务
os.popen(adb_path + " kill-server")
os.popen(adb_path + " start-server")

# 2、检测连接设备列表
res = os.popen(adb_path + " devices")
print res.read()

# 3、
while True:
    os.popen(adb_path + " -s 6HJDU20214024902 shell input swipe 350 1300 600 500 400")
    time.sleep(3)
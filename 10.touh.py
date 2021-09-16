#coding:utf-8

import RPi.GPIO as GPIO
import time

# 触摸传感器的信号引脚
touchPin = 11
# 激光模块的信号引脚
lightPin = 12

# 设置采用物理编码
GPIO.setmode(GPIO.BOARD)
# 对触摸传感器的引脚进行初始化
GPIO.setup(touchPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# 对激光传感器的引脚进行初始化
GPIO.setup(lightPin,GPIO.OUT)

while True:
    swi = GPIO.input(touchPin)
    # 当触摸发生时，触摸传感器的引脚输入高电平 
    if swi == 1:
        # 向激光模块的引脚输出高电平，发射激光
        GPIO.output(lightPin, GPIO.HIGH)
    else:
        # 与上面相反，关闭激光
        GPIO.output(lightPin, GPIO.LOW)
    time.sleep(0.5)
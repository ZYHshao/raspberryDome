#coding:utf-8

import RPi.GPIO as GPIO
import time

# 触发声波引脚
trig = 11
# 监听信号
echo = 12

def getDistance():
	# 输出高电平
	GPIO.output(trig, GPIO.HIGH)
	# 持续15us高电平 触发超声波
	time.sleep(0.000015) 
	# 停止加高电平
	GPIO.output(trig, GPIO.LOW)

	# 开始检测信号引脚的电平为高电平时开始计时
	while GPIO.input(echo) == 0:
		pass
	t1 = time.time()
	# 信号引脚的电平为低电平时计算时间间隔
	while GPIO.input(echo) == 1:
		pass
	t2 = time.time()
	# 计算距离
	s = (t2 - t1)*340/2
	return s

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	s = getDistance()
	print("当前距离前方障碍物：%fm"%(s))
	time.sleep(1)
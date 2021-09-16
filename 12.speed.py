#coding:utf-8

import RPi.GPIO as GPIO
import time
# 采用物理编码
GPIO.setmode(GPIO.BOARD)
# BCM GPIO17的物理编码是11
out_pin = 11
# 0 计数模式 1 测速模式
MODE = 0
count = 0
# 测速模式下，需要初始化长度S 单位为毫米
S = 10
t1 = 0
t2 = 0

# 进行引脚的初始化，不被遮挡时为低电平，使用低电平的下拉电阻
GPIO.setup(out_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# 定义回调函数
def switch_state(pin):
	global count,t1,t2
	# 如果是高电平
	if GPIO.input(pin):
		print("物体遮挡")
		if MODE == 0:
			count += 1
		else:
			t1 = time.time()
	else:
		print("物体遮挡消失")
		if MODE == 0:
			print('计数器-数量：%d'%(count))
		else:
			t2 = time.time()
			t = t2 - t1
			v = S / t
			print('测速器-速度%fmm/s'%(v))

GPIO.add_event_detect(out_pin, GPIO.BOTH, callback=switch_state)

while True:
	pass
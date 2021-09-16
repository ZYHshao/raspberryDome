#coding:utf-8

# 导入GPIO控制薄块
import RPi.GPIO as GPIO
# 导入time模块
import time


# 设置使用的引脚编码模式
GPIO.setmode(GPIO.BOARD)

# 定义开关引脚
swi = 29
# 定义蜂鸣器引脚
fm = 13
# 进行开关引脚的初始化，设置为输入引脚，且默认为高电平
GPIO.setup(swi, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# 进行蜂鸣器引脚的初始化，因为是低电平触发，初始时设置为高电平
GPIO.setup(fm,GPIO.OUT, initial=GPIO.HIGH)
# 定义状态变化的回调函数
def switch(channel):
	# 高电平的开关松开
	if GPI0.input(channel):
		GPIO.output(fm, GPIO.HIGH)
	# 低电平为开关按下
	else:
		GPIO.output(fm, GPIO.LOW)
		
# 添加输入引脚电平变化的回调函数
GPIO.add_event_detect(swi, GPIO.BOTH, callback=switch, bouncetime=200)
# 开启循环
while True:
	pass














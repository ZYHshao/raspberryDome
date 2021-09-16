#coding:utf-8
import pcf8591 as PCF
import RPi.GPIO as GPIO
import time

DO = 11
# 设置使用的引脚编码模式
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DO, GPIO.IN)
PCF.init(0x48)
while True:
	print('------------分割线-------------')
	rainDO = GPIO.input(DO)
	print('是否检测到水滴：%s'%('否' if rainDO else '是'))
	# 读取AIN0的模拟数据
	rainAO = PCF.read(0) 
	print('雨水程度%d'%(255 - rainAO))
	time.sleep(2)
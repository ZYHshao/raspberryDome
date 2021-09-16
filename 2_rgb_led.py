#coding:utf-8

# 导入GPIO控制薄块
import RPi.GPIO as GPIO
# 导入time模块
import time
# 导入系统模块
import sys

# 定义引脚
R,G,B = 12,35,38
# 设置使用的引脚编码模式
GPIO.setmode(GPIO.BOARD)

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)

# 使用PWM脉冲宽度调制
pR = GPIO.PWM(R, 60)
pG = GPIO.PWM(G, 60)
pB = GPIO.PWM(B, 60)

pR.start(0)
pG.start(0)
pB.start(0)

# 初始时，各种颜色点亮2秒
pR.ChangeDutyCycle(100)
pG.ChangeDutyCycle(0)
pB.ChangeDutyCycle(0)
time.sleep(2)

pR.ChangeDutyCycle(0)
pG.ChangeDutyCycle(100)
pB.ChangeDutyCycle(0)
time.sleep(2)

pR.ChangeDutyCycle(0)
pG.ChangeDutyCycle(0)
pB.ChangeDutyCycle(100)
time.sleep(2)

endTime = 100
current = 0

# 开始进行炫彩闪烁
while True:
	for r in range(0, 101, 10):
		pR.ChangeDutyCycle(r)
		for g in range(0, 101, 10):
			pG.ChangeDutyCycle(g)
			for b in range(0, 101, 10):
				pB.ChangeDutyCycle(b)
				time.sleep(0.1)
				current += 1
				if (current > endTime):
					pR.stop()
					pG.stop()
					pB.stop()
					GPIO.cleanup()
					sys.exit(0)












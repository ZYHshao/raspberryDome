#coding:utf-8
import time
import smbus
BUS = smbus.SMBus(1)
# LCD屏幕的硬件地址
LCD_ADDR = 0x27
# 是否开启背光 由PCF8574T的低4位中的第4位决定
BLEN = 1 

# 补充背光控制位
def addBlenControl(data):
    global BLEN
    tmpData = data
    if BLEN:
        # 将第4位背光控制位强制设置1
        tmpData = data | 0b00001000
    else:
        # 将第4位背光控制位强制设置为0
        tmpData = data & 0b11110111
    return tmpData    

# 补充Enable控制位
def addEnableControl(data, high):
    tempData = data
    # 第3位控制Enable
    if high:
        tempData |= 0b00000100
    else:
        tempData &= 0b11111011
    return tempData

# 补充RS控制位
def addRSControl(data, high):
    tempData = data
    # 第1位控制RS
    if high:
        tempData |= 0b00000001
    else:
        tempData &= 0b11111110
    return tempData

# 通过I2C总线写入数据
def writeI2C(addr, data):
    # 添加背光控制
    temp = addBlenControl(data)
    # 写数据到I2C总线
    BUS.write_byte(addr ,temp)

# 发送指令到LCD1602
def sendCommand(comm):
    # comm高4位数据传输
    # 低4位先清空
    buf = comm & 0b11110000
    # 先将Enable置为高电平
    buf = addEnableControl(buf, 1)
    # 设置为指令模式
    buf = addRSControl(buf, 0)
    # 写入指令
    writeI2C(LCD_ADDR ,buf)
    time.sleep(0.002)
    # 将Enable置为低电平 使产生低电平跳变来执行指令
    buf = addEnableControl(buf, 0)          
    writeI2C(LCD_ADDR ,buf)
     
    # comm低4位数据传输
    # 高4位先清空 并将低4位的数据移动到高4位
    buf = (comm & 0b00001111) << 4
    # 当次指令的低4位用来 做enable re rew的控制
    # 先将Enable置为高电平
    buf = addEnableControl(buf, 1)
    writeI2C(LCD_ADDR ,buf)
    time.sleep(0.002)
    # 将Enable置为低电平 使产生低电平跳变来执行指令
    buf = addEnableControl(buf, 0)     
    writeI2C(LCD_ADDR ,buf)

# 发送数据到LCD 
def sendData(data):
    # data高4位数据传输
    # 低4位先清空
    buf = data & 0b11110000
    # 先将Enable置为高电平
    buf = addEnableControl(buf, 1)
    # 设置为数据模式
    buf = addRSControl(buf, 1)   
    writeI2C(LCD_ADDR ,buf)
    time.sleep(0.002)
    # 将Enable置为低电平 使产生低电平跳变来执行指令
    buf = addEnableControl(buf, 0)  
    writeI2C(LCD_ADDR ,buf)
     
    # data低4位数据传输
    buf = (data & 0b00001111) << 4
    # 先将Enable置为高电平
    buf = addEnableControl(buf, 1)
    # 设置为数据模式
    buf = addRSControl(buf, 1) 
    writeI2C(LCD_ADDR ,buf)
    time.sleep(0.002)
    # 将Enable置为低电平 使产生低电平跳变来执行指令
    buf = addEnableControl(buf, 0)  
    writeI2C(LCD_ADDR ,buf)

# 初始化方法
def initLCD():
    # 启动时，LCD1602为8位模式 I2C传输数据时先传输的为低位数据
    # 因此实际上的指令为 0b00100011
    # 为指令6 将LCD1602设置为4位总线模式
    sendCommand(0b00110010) 
    time.sleep(0.005)

    # 之后的指令都是4位总线模式
    sendCommand(0b00110010) 
    time.sleep(0.005)
    # 指令4 设置屏幕开启，无光标，无闪烁
    sendCommand(0b00001100)
    time.sleep(0.005)
    # 指令1 清屏
    sendCommand(0b00000001) 

# 设置屏幕要展示的文案 x，y确定位置
def printLCD(x, y, str):
    # 2行 16 列
    if x < 0:
        x = 0
    if x > 15:
        x = 15
    if y <0:
        y = 0
    if y > 1:
        y = 1
    # 指令7 设置数据要展示的位置
    addr = 0b10000000 + 0b00000100 * y + x
    sendCommand(addr)
    # 开始发送字符数据到LCD1602的数据寄存器
    for chr in str:
        # ord函数可以获取字符的ascil
        sendData(ord(chr))
 
# 主程序
initLCD()
printLCD(0, 0, 'Hello, world!')
time.sleep(2)
sendCommand(0b00000001)
time.sleep(0.002)
printLCD(0, 0, 'Love China!')
time.sleep(2)
sendCommand(0b00000001)
time.sleep(0.002)
printLCD(0, 0, 'Great Raspberry!')
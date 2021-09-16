#coding:utf-8

#SMBus (System Management Bus,系统管理总线) 
import smbus   #在程序中导入“smbus”模块
import time

bus = smbus.SMBus(1)         #创建一个smbus实例

# 数据读取的方法
def read(chn): #channel
    if chn == 0:
        #发送一个控制字节到设备 表示要读取AIN0通道的数据
        bus.write_byte(0x48,0x40)   
    if chn == 1:
        #发送一个控制字节到设备 表示要读取AIN1通道的数据
        bus.write_byte(0x48,0x41)
    if chn == 2:
        #发送一个控制字节到设备 表示要读取AIN2通道的数据
        bus.write_byte(0x48,0x42)
    if chn == 3:
        #发送一个控制字节到设备 表示要读取AIN3通道的数据
        bus.write_byte(0x48,0x43)
    bus.read_byte(0x48)         # 空读一次，消费掉无效数据
    return bus.read_byte(0x48)  # 返回某通道输入的模拟值A/D转换后的数字值

if __name__ == "__main__":
    while True:
        print('电位计 AIN3 = ', 0.196 * read(3))   #电位计模拟信号转化的数字值
        print('光敏电阻 AIN0 = ', 255 - read(0))   #光敏电阻模拟信号转化的数字
        print('热敏电阻 AIN1 = ',255-read(1))      #热敏电阻模拟信号转化的数字值
        time.sleep(2)
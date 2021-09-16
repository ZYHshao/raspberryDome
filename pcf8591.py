#coding:utf-8
import smbus   #在程序中导入“smbus”模块
# /dev/i2c-1
bus = smbus.SMBus(1)  #创建一个smbus实例

# 初始化驱动模块 定义PCF元件地址
def init(addr):
	global address
	address = addr

# 读取某个通道的数据
def read(chn):
	global address
	if chn == 0:
		#发送一个控制字节到设备 表示要读取AIN0通道的数据
		bus.write_byte(address,0x40)   
	if chn == 1:
		#发送一个控制字节到设备 表示要读取AIN1通道的数据
		bus.write_byte(address,0x41)
	if chn == 2:
		#发送一个控制字节到设备 表示要读取AIN2通道的数据
		bus.write_byte(address,0x42)
	if chn == 3:
		#发送一个控制字节到设备 表示要读取AIN3通道的数据
		bus.write_byte(address,0x43)
	bus.read_byte(address)         # 空读一次，消费掉无效数据
	return bus.read_byte(address)  # 返回某通道输入的模拟值A/D转换后的数字值

def write(val):
	global address
	temp = val
	temp = int(temp) 
	# 进行写数据操作
	bus.write_byte_data(address, 0x40, temp) 
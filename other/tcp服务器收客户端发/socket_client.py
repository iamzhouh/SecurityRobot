import socket
import os

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('175.27.245.39', 12000))  # 链接服务器的ip + 端口

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获得当前目录

while True:
	img_name = 'a.jpg'
	img_path = '/home/pi/Desktop/'
	img_path = img_path+img_name
	file_size = os.stat(img_path).st_size  # 获得图像文件的大小，字节单位   调用 stat 时用来返回相关文件的系统状态信息
	file_info = '%s|%s' % (img_name, file_size)  # 将图像信息发给服务端（用于区分文档中的两个任务）
	client.sendall(bytes(file_info, 'utf-8'))

	f = open(img_path, 'rb')  # 以二进制格式打开一个文件用于只读
	has_sent = 0  # 记录下已经发送的字节数
	while has_sent != file_size:  # 发送的字节数 不等于 图像的大小，则接着发送
		file = f.read(1024)  # 一次读1024个字节
		client.sendall(file)  # 发送给服务端
		has_sent += len(file)  # 更新已发送的字节数
	f.close()  # 发送结束，关闭文件
	print('上传成功')
	break

client.close()
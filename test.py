from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import socket  # 导入 socket 模块
import mess_pb2

t = mess_pb2.test()
t.cmd = 0
t.inform = "hello"

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 9123  # 设置端口号

s.connect((host, port))

wData = QByteArray()
data = QDataStream(wData, QIODevice.WriteOnly)

data.writeInt32(socket.htonl(len(t.SerializeToString())))

data.writeRawData(t.SerializeToString())
print(wData.data())
s.send(wData.data())
# s.send(wData.data())
# s.send(wData.data())

print(s.recv(1024))
s.close()

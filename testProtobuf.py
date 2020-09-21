import mess_pb2

mess = mess_pb2.qwe()
mess.cmd = 1
mess.str = "hello"

print(mess.SerializeToString())

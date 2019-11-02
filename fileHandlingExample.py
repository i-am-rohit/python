import time
fs=open("prog1.py",'r')
print("sucess")
print(fs.readable(),fs.writable(),fs.seekable())
print(fs.tell())
data=fs.read()
print(data)
print(fs.tell())

# data=fs.read()
# print(data)
# while(True):
#     data=fs.read(5)
#     if(data==''):
#         break
#     print(data,end='')
#     time.sleep(1)

import time
fs=open(r"c:\abc\abc.csv",'w')
print("sucess")
list1=["id","name","Address","Mobile No"]
for e in list1:
    fs.write(e+",")
fs.close()
# while(True):
#     data=input("Enter String for write 0 for Exit")
#     if(data=='0'):
#         break
#     fs.write(data+"\n")
#     fs.flush()
# fs.close()


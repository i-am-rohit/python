class Class1:
    def __init__(self):
        self.x=0
        self.y=0
    def __str__(self):
        return "X:"+str(self.x)+" Y:"+str(self.y)

ob1=Class1()
x=5
ob1.x=100
ob1.y=200
print(x)
# y=ob1.__str__()
print(ob1)
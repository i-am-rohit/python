a = int(input("enter length : "))
b = int(input("enter breadth : "))
class area:
    def __init__(self,length,breadth):
        self.length = length    
        self.breadth = breadth
    
    def rectangle(self):
        return self.length * self.breadth

obj = area(a,b)
print(obj.rectangle())



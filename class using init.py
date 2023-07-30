class batch:

    def __int__(self, a,b,c):
        self.name = a
        self.clas = b
        self.special = c

    def info(self):
        print(f"{a} is pursuing {b} in {c} ")


a = input("enter the name : ")
b = input("enter the class : ")
c = input("enter the specialization : ")

d = batch()
d.info()
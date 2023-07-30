#BLL
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def Mul(self):
        print(self.a * self.b)

    def sub(self):
        print(self.a - self.b)

    def div(self):
        print(self.a / self.b)



#PLL


a = int(input("enter first number : "))
b = int(input("enter Second number : "))

ent = Calculator(a,b)


choice = 1
while choice != 0:

    print("0 : EXIT")
    print("1 : SUM")
    print("2 : Subtract")
    print("3 : Divide")
    print("4 : Multiply")
    choice = int(input("enter your choice : "))

    if choice == 1:
        print("Sum : ", ent.add())

    elif choice == 2:
        print("Subtract : ", ent.sub())

    elif choice == 3:
        print("Divide : ", ent.div())

    elif choice == 4:
        print("Multiplication : ", ent.Mul())

    elif choice == 0:
        print("exiting!")

    else:
        print("Invalid Choice!")




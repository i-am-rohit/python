class Customer:
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.address=''
        self.mob=''

    def __str__(self):
        return "ID: "+str(self.id)+" Name: "+self.name+" Address: "+self.address+" Mobile No: "+self.mob
    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for cus in Customer.listCus:
            if(cus.id==id):
                self.name=cus.name
                self.address=cus.address
                self.mob=cus.mob
                return
    def deleteCustomer(self,id):
        for cus in Customer.listCus:
            if(cus.id==id):
                Customer.listCus.remove(cus)
                return
        print("Id not found")
    def getAllCustomer(self):
        return Customer.listCus
    # def deleteCustomer(self,id):
    #     for i in range(len(Customer.listCus)):
    #         if(cus.id==id):
    #             Customer.listCus.remove(cus)
    #             return
    #     print("Id not found")


#PL Code Start from HERE
def showAllCustomer():
    cus=Customer()
    for cus in cus.getAllCustomer():
        print(cus)
while(True):
    print("1.Add\n2.Search\n3.Delete Customer\n5.Show All Customer\n0.Exit")
    ch=input("Enter ur choice")
    if(ch=='1'):
        cus=Customer()
        cus.id=int(input("Enter Id"))
        cus.name=input("Enter Name")
        cus.address = input("Enter Address")
        cus.mob = input("Enter Mobile No")
        cus.addCustomer()
        print("Customer Added Sucessfully")

    elif(ch=='2'):
        cus=Customer()
        id=int(input('Enter ID'))
        cus.searchCustomer(id)
        print(cus)

    elif (ch == '3'):
        cus = Customer()
        id = int(input('Enter ID'))
        cus.deleteCustomer(id)
        print("Customer Delted Sucessfully")
    elif (ch == '5'):
        showAllCustomer()

    else:
        break
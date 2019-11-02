import pickle
class Customer:
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=''
        self.address=''
        self.mob=''
    def __str__(self):
        return "id:"+str(self.id)+" Name:"+self.name+" Address"+ self.address+" mobileno: "+self.mob

    @staticmethod
    def saveDatainFile():
        listinBytes=pickle.dumps(Customer.listCus)
        fs=open("CusMgrPickle.txt",'wb')
        fs.write(listinBytes)
        fs.close()

    @staticmethod
    def loadDatafromFile():
        fs = open("CusMgrPickle.txt", 'rb')
        listinBytes = fs.read()
        Customer.listCus=pickle.loads(listinBytes)

    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for cus in Customer.listCus:
            if(cus.id==id):
                self.id=cus.id
                self.name=cus.name
                self.address=cus.address
                self.mob=cus.mob
                return

        raise Exception("Id not found")#Wrong code handle in Exception Handling

    def deleteCustomer(self,id):
        for i in range(len(Customer.listCus)):
            if (Customer.listCus[i].id == id):
                Customer.listCus.pop(i)
                return

        print("Id not found")  # Wrong code handle in Exception Handling
    @staticmethod
    def sortingKey(cus):
        return cus.id
    @staticmethod
    def sortCustomer():
        Customer.listCus.sort(key=Customer.sortingKey)
    @staticmethod
    def getCustomers():
        return Customer.listCus
def showAllCustomers():
    for cus in Customer.getCustomers():
        print(cus)

if(__name__=="__main__"):

    while(True):
        print("1.Add Customer\n2.Search Customer\n3.Modify Customer\n4.Delete Customer\n5.Show All\n6.Sort Customer\n7.Save Data in File\n8.Load Data from file\n0.Exit")
        ch = input("Enter ur Choice")
        if(ch=='1'):
            try:
                cus=Customer()
                cus.id=int(input("Enter Id"))
                cus.name=input("Enter Name")
                cus.address = input("Enter Address")
                cus.mob = input("Enter Mobile No")
                cus.addCustomer()
                print("Customer Added Sucessfully")
            except Exception as ex:
                print(ex)


        elif(ch=='2'):
           try:
                cus=Customer()
                id = int(input("Enter Id"))
                cus.searchCustomer(id)
                print(cus)
           except Exception as ex:
               print(ex)
        elif(ch=='3'):
            pass
            # id = int(input("Enter Id"))
            # name = input("Enter Name")
            # address = input("Enter Address")
            # mob = input("Enter Mobile No")
            # modifyCustomer(id, name, address, mob)
            # print("Customer Added Sucessfully")

        elif(ch=='4'):
            try:
                cus=Customer()
                id = int(input("Enter Id"))
                cus.deleteCustomer(id)
                print("Customer Delted Sucessfully")
            except Exception as ex:
                print(ex)
        elif (ch == '5'):
            # print(Customer.listCus)
            showAllCustomers()
        elif (ch == '6'):
            # print(Customer.listCus)
            Customer.sortCustomer()
        elif (ch == '7'):
            # print(Customer.listCus)
            Customer.saveDatainFile()
        elif (ch == '8'):
            # print(Customer.listCus)
            Customer.loadDatafromFile()

        elif(ch=='0'):
            break

import pickle
import json
class Customer:
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=None
        self.address=None
        self.mob=None
    @staticmethod
    def convertCustomerIntoDict(cus):
        return cus.__dict__

    @staticmethod
    def saveDataInFile():
        fs=open("CusMgtjson.txt",'w')
        json.dump(Customer.listCus,fs,default=Customer.convertCustomerIntoDict)

    @staticmethod
    def convertDictIntoCustomerAuto(dictCus):
        cus = Customer()
        for e in dictCus.items():
            cus.__setattr__(e[0], e[1])
        return cus

    @staticmethod
    def loadDatafromFile():
        fs = open("CusMgtjson.txt",'r')
        Customer.listCus=json.load(fs,object_hook=Customer.convertDictIntoCustomerAuto)

    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                self.id=e.id
                self.name=e.name
                self.address=e.address
                self.mob=e.mob
                return
        raise Exception("Id not found")
    def deleteCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                Customer.listCus.remove(e)
                return
        print("Id not found")

    def modifyCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if (Customer.listCus[i].id == id):
                Customer.listCus[i]=self
                return
        print("Id not found")
    @staticmethod
    def showAllCustomer():
        for e in Customer.listCus:
            print("id:",e.id,"Name:",e.name,"Address:",e.address,"Mobile No:",e.mob)

if(__name__=="__main__"):

    while(True):
        print("1.Add Customer\n2.Search Customer\n3.Delete Customer\n4.Modify Customer\n6.Save Data in File\n7Load Data from File\n8ShowAllCustomer\n0.Exit")
        ch=input("Enter your Choice")
        if(ch=='1'):
            try:
                cus=Customer()
                cus.id=int(input('Enter Id'))
                cus.name=input("Enter Name")
                cus.address=input("Enter Address")
                cus.mob=input("Enter Mobile No")
                cus.addCustomer()
                print("Customer Added Sucessfully")
            except Exception as ex:
                print(ex)

        elif(ch=='2'):
            try:
                cus = Customer()
                id = int(input('Enter Id'))
                cus.searchCustomer(id)
                # print(cus)
                print("Id:",cus.id," Name:",cus.name,"Address: ",cus.address,"Mobile No:",cus.address)
            except Exception as ex:
                print(ex)

        elif (ch == '3'):
            pass
        elif (ch == '4'):
            pass
        elif (ch == '6'):
            Customer.saveDataInFile()
        elif (ch == '7'):
            Customer.loadDatafromFile()
        elif (ch == '8'):
            Customer.showAllCustomer()

        else:
            break
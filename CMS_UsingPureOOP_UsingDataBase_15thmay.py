import pymysql
class Customer:
    con = pymysql.connect(host="localhost", user="root", password="root123", database='15maydb')
    def __init__(self):
        self.id=0
        self.name=''
        self.address=''
        self.mob=''
    def __str__(self):
        return "id:"+str(self.id)+" Name:"+self.name+" Address"+ self.address+" mobileno: "+self.mob

    def addCustomer(self):
        myCursor = Customer.con.cursor()
        strQuery = "insert into Customer values(%s,%s,%s,%s)"
        myCursor.execute(strQuery, (self.id, self.name, self.address, self.mob))
        Customer.con.commit()

    def searchCustomer(self,id):
        myCursor = Customer.con.cursor()
        strQuery = "select * from Customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.id = row[0]
            self.name = row[1]
            self.address = row[2]
            self.mob = row[3]
        else:
            raise Exception("Id not found")#Wrong code handle in Exception Handling

    def searchCustomer2(self, id):
        for i in range(len(Customer.listCus)):
            if (Customer.listCus[i].id == id):
                self.id = Customer.listCus[i].id
                self.name = Customer.listCus[i].name
                self.address = Customer.listCus[i].address
                self.mob = Customer.listCus[i].mob
                return

        print("Id not found")  # Wrong code handle in Exception Handling
    def delCustomer2(self,id):
        for cus in Customer.listCus:
            if (cus.id == id):
                Customer.listCus.remove(cus)
                return

        print("Id not found")  # Wrong code handle in Exception Handling
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

while(True):
    print("1.Add Customer\n2.Search Customer\n3.Modify Customer\n4.Delete Customer\n5.Show All\n6.Sort Customer\n0.Exit")
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

    elif(ch=='0'):
        break

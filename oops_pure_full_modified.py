class costumer:
    cost = []

    def __init__(self):
        self.id = 0
        self.name = " "
        self.address = " "
        self.mob = " "

    def __str__(self):
        return "ID: "+str(self.id)+" Name: "+self.name+" Address: "+self.address+" Mobile No: "+self.mob

    def get_data(self):
        return costumer.cost

    def add_data(self):
        costumer.cost.append(self)
        return

    def search_data(self,id):
        for cus in costumer.cost:
            if(cus.id == id):
                self.id = cus.id
                self.name = cus.name
                self.address = cus.address
                self.mob = cus.mob
                return

    def delete_data(self,id):
        for cus in costumer.cost:
            if(cus.id==id):
                costumer.cost.remove(cus)
                return


    def modify_data(self):
        for cus  in costumer.cost:
            if(cus.id == id):
                cus.name = self.name
                cus.address = self.address
                cus.mob = self.mob
                return


def show_data():
    cus =costumer()
    for cus in  cus.get_data():
        print(cus)

while(True):
    print(" 1.SHOW DATA \n 2.ADD DATA \n 3.SEARCH_DATA \n 4.DELETE_DATA \n 5.MODIFY DATA \n 6.EXIT ")
    ch = int(input("ENTER YOUR CHOICE : "))

    if (ch==1):
        show_data()

    elif (ch==2):
        cus = costumer()
        cus.id = int(input("ENTER ID : "))
        cus.name = input("ENTER NAME : ")
        cus.address = input("ENTER ADDRESS : ")
        cus.mob = input("ENTER MOBILE : ")
        cus.add_data()
        print("successfully added")

    elif (ch==3):
        cus = costumer()
        id = int(input("ENTER ID : "))
        cus.search_data(id)
        print(cus)

    elif (ch==4):
        cus = costumer()
        id = int(input("ENTER ID : "))
        cus.delete_data(id)
        print("deleted successfully")

    elif (ch==5):
        cus = costumer()
        id = int(input("ENTER ID : "))
        cus.name= input("ENTER NEW NAME : ")
        cus.address = input("ENTER NEW ADDRESS : ")
        cus.mob =input("ENTER NEW MOBILE : ")
        cus.modify_data()
        print("modify successfully")

    elif (ch==6):
        exit()






# BLL LAYER
listid = []
listname= []
listadd = []
listphone = []

def add_entity(id,name,address,phone):
    listid.append(id)
    listname.append(name)
    listadd.append(address)
    listphone.append(phone)
    print(listid,listname,listadd,listphone)
    return

def search_entity(id):
    if(listid.__contains__(id)):
        i = listid.index(id)
        print("ID = ", listid[i], "Name = ", listname[i], "Address = ", listadd[i], "Phone = ", listphone[i])

    else:
        print("ENTITY NOT FOUND")

def delete_entity(id):
    if(listid.__contains__(id)):
        i = listid.index(id)
        listid.pop(i)
        listname.pop(i)
        listadd.pop(i)
        listphone.pop(i)
    else:
        print("ENTITY NOT FOUND")

def modify_entity(id,name,address,phone):
    if (listid.__contains__(id)):
        i = listid.index(id)
        if(name != "na"):
            listname[i] = name
        elif(address != "na"):
            listadd[i] = address
        elif(phone != "na"):
            listadd[i] = phone
    print("MODIFICATION COMPLETED")



# BLL LAYER


# PL LAYER
while(True):
    print(" 0.SHOW ENTITY \n 1.ADD ENTITY \n 2.SEARCH ENTITY \n 3.DELETE ENTITY \n 4.MODIFY ENTITY ")
    ch = input("enter your choice : ")
    if(ch=="0"):
        print(listid,listname,listadd,listphone)

    if(ch=="1"):
        id = int(input("enter id : "))
        name = input("enter name: ")
        address = input("enter address : ")
        phone = input("enter phone : ")
        add_entity(id,name,address,phone)
        print("entity successfully added")

    if(ch=="2"):
        id = int(input("enter id do you want to search : "))
        search_entity(id)

    if(ch=="3"):
        id = int(input("enter id do you want to remove : "))
        delete_entity(id)
        print("entity succesfully deleted")

    if(ch=="4"):
        print(" 1.MODIFY NAME \n 2.MODIFY ADDRESS \n 3.MODIFY PHONE")
        ch1 =input("enter your choice")
        if(ch1=="1"):
            id = int(input("enter id to modify"))
            name = input("enter new entity")
            modify_entity(id,name,"na","na")
        elif(ch1=="2"):
            id = int(input("enter id to modify"))
            address = input("enter new address")
            modify_entity(id, "na", address, "na" )
        elif(ch1=="3"):
            id = int(input("enter id to modify"))
            phone = input("enter new phone")
            modify_entity(id, "na", "na", phone )
        print("modification done")
# PL LAYER
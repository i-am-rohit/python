import json
from Cms_Project_OOP import Customer
def convertDictIntoCustomerAuto(dictCus):
    cus=Customer()
    for e in dictCus.items():
        cus.__setattr__(e[0],e[1])
    return cus

def convertDictIntoCustomer(dictCus):
    cus=Customer()
    cus.id=dictCus['id']
    cus.name=dictCus['name']
    cus.address=dictCus['address']
    cus.mob=dictCus['mob']
    return cus
def ConvertCustomerIntoDict(cus):
    return cus.__dict__
#Json Serialization Start
cusdataInPython=Customer()
cusdataInPython.id=40
cusdataInPython.name="abc40"
cusdataInPython.address="xyz40"
cusdataInPython.mob="94"
dataInPython=ConvertCustomerIntoDict(cusdataInPython)


dataAfterSerialization=json.dumps(dataInPython)
print(type(cusdataInPython),dataInPython,type(dataInPython))
print( dataAfterSerialization,type(dataAfterSerialization))
#Json Serialization Ends

#Json DeSerialization Start
print("Result After DeSerialization")
dataAfterDeserialization=json.loads(dataAfterSerialization)
# convertDictIntoCustomerAuto(dataAfterDeserialization)
cusAfterDeseialization=convertDictIntoCustomerAuto(dataAfterDeserialization)
print(dataAfterSerialization,type(dataAfterSerialization))
print(type(cusAfterDeseialization),dataAfterDeserialization,type(dataAfterDeserialization))

#Json DeSerialization Ends
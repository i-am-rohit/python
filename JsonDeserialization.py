import json
from CMS_UsingPureOOP import Customer
def convertDictIntoCustomer(cusInDict):
     cus=Customer()
     cus.id=cusInDict["id"]
     cus.name=cusInDict["name"]
     cus.address=cusInDict["address"]
     cus.mob=cusInDict["mob"]
     return cus


def convertDictIntoCustomer_Auto(cusInDict):
    cus = Customer()
    for e in cusInDict.items():
        cus.__setattr__(e[0],e[1])
    return cus

# cus=Customer()
# cus.id=5
# cus.__setattr__("name","abc5")
# print()

fs=open("CmsProjectJson.txt",'r')
jsonString=fs.read()
cusInDict=json.loads(jsonString)
cus=convertDictIntoCustomer_Auto(cusInDict)
print(cus)

import json
#Json Serialization Start
dataInPython=5
dataInPython=5.5
dataInPython=[1,4,"abcd",5.6,7]
dataInPython=(1,4,"abcd",5.6,7)
dataInPython={1:"aaa",4:"bbb",5:"abcd"}
dataInPython=[{"id":5,"Name":"abc5"},{"id":7,"Name":"abc7"}]
dataAfterSerialization=json.dumps(dataInPython)
print(dataInPython,type(dataInPython))
print(dataAfterSerialization,type(dataAfterSerialization))
#Json Serialization Ends

#Json DeSerialization Start
print("Result After DeSerialization")
dataAfterDeserialization=json.loads(dataAfterSerialization)
print(dataAfterSerialization,type(dataAfterSerialization))
print(dataAfterDeserialization,type(dataAfterDeserialization))

#Json DeSerialization Ends
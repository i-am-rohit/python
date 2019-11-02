import pymysql
con=pymysql.connect(host="localhost",user = "root",password="Yes",database="new_project")
# print("success")
# print(type(con))
mycursor = con.cursor()
strquery = "select* from costumer"
rowaffected = mycursor.execute(strquery)
print(mycursor.fetchall())
# print(mycursor.description())


for row in mycursor.description():
    print(row[0],end='\t')
print()
for row in mycursor.fetchall():
    for cell in row:
        print(cell,end="\t")
    print()
print(rowaffected)

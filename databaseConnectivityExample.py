
import pymysql
x=0x45

con= pymysql.connect(host="localhost",user="root",password="root123",database="29thmay")
print("Sucess")
myCursor=con.cursor()
strQuery="select * from customer"
rowAffected=myCursor.execute(strQuery)

# data=myCursor.fetchall()
# print(data)
# data=myCursor.description
# print(data)
fs=open(r"c:\abc\abc.csv",'w')
for row in myCursor.description:
    print(row[0],end='\t')
    fs.write(row[0]+",")
fs.write("\n")
print()
for row in myCursor.fetchall():
    for cell in row:
        fs.write(str(cell)+",")
        print(cell,end='\t')
    print()
    fs.write("\n")

fs.close()
    # print(row)
print("Total Record=",rowAffected)
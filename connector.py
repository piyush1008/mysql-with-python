import mysql.connector
mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="Piyu$h98.",
     database="db1"   ## create the database db1 through mysql command client
    )

#print(mydb.connection_id) ### to check wether the connection is establish or not

cur=mydb.cursor() ## it is required to do curd operation.

##creating the table book
#s="create table book(bookid integer(4),title varchar(20),price float(5,2))";
#cur.execute(s)

## inserting in the book table

#ins="insert into book(bookid,title,price) values(%s,%s,%s)"
#b1=(1,'python2',222) #inserting single record
#cur.execute(ins,b1)

#b2=[(2,"php",232),(3,"java",898)]
#cur.executemany(ins,b2) ## inserting many record in the table.



## extracting the records from the table
'''
s="select * from book "
cur.execute(s)
result=cur.fetchall()
for res in result:
    print(res)
'''

## updating records in the table
'''
s="update  book set price=456 where bookid=1"
cur.execute(s)

'''

##deleting the records from the table
s="delete from book where bookid=1"
cur.execute(s)
mydb.commit()

#cur.execute('''create database db1 ''')

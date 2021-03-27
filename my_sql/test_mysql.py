import logging
import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shiv@123",
            database="student",
            auth_plugin="mysql_native_password")

logging.basicConfig(filename='newfile.log',filemode='w',format='%(levelname)s::%(message)s::%(lineno)d',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

try:
    print("connection is successful ",mydb.is_connected())

except TypeError as e:
    logging.error("connection is not successful",e)

mycursor = mydb.cursor()

def getdata():
    try:
        query=input("Please enter query to display data from database =")
        mycursor.execute(query)
        for x in mycursor:
            print("data=",x)
        logging.info("data displayed sussefully")
    except:
        logging.error("something went wrong check your query syntax and database table and data inside it")

def insertdata():
    try:
        query=input("Please enter query to insert data (insert into table,update,delete)=")
        mycursor.execute(query)
        mydb.commit()
        logging.info("data insearted sucessfully into database")
    except:
        logging.error("something went wrong please check your database and query syntax carefully")

def update():
    try:
        query=input("enter query to update data into table = ")
        mycursor.execute(query)
        mydb.commit()
        logging.info("data updated sucessfully into student_detail of student database")
    except:
        logging.error("data not fund or query syntax error")

while True:
    print("please select operation")
    print("[1] for display data from database")
    print("[2] for insert data into database")
    print("[3] for update table ")
    print("[4] for exit")

    userInput=int(input("enter your choice="))
    if userInput==1:
        getdata()
    elif userInput==2:
        insertdata()
    elif userInput==3:
        update()
    else:
        value="False"
        break

#test=Test_db()
mycursor.close()
mydb.close()

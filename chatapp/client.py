import threading
import socket
import mysql.connector

alias = input('Choose an alias >>> ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shiv@123",
    database="chat",
    auth_plugin="mysql_native_password")

try:
    print("connection is successful ",mydb.is_connected())

except TypeError as e:
    print("connection is not successful",e)

mycursor = mydb.cursor()


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            string_message=str(message)
            query = input("insert into talking (chat)values(?)",(string_message,))
            mycursor.execute(query)
            mydb.commit()

            if message == "alias?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send():
    while True:
        message = f'{alias}: {input("")}'
        string_message = str(message)
        query = input("insert into talking (chat) values (?)", (string_message,))
        mycursor.execute(query)
        mydb.commit()

        client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

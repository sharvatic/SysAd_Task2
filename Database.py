import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE studentdetails")

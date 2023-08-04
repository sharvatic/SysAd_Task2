import mysql.connector
db = mysql.connector.connect( 
    host = "localhost", 
    user = "root", 
    passwd = "admin@123", 
    database = "studentDetails" 
) 

mycursor = db.cursor()
TableName = 'Details'
file = open('/var/www/gamma-z.hm/studentDetails.txt')
file_content = file.readlines() ;
values = [line.split() for line in file_content]

createStatement='CREATE TABLE '+ TableName + '('
i=0
while i< len(values[0])-1 :

    createStatement =createStatement + values[0][i] +'  '+'VARCHAR(15)'+', '
    i=i+1

createStatement =createStatement +values[0][i] +'  '+'VARCHAR(15)'+' );'

#print(createStatement)
mycursor.execute(createStatement)

query = "INSERT INTO "+ TableName + " (Name, RollNumber, Hostel, Room, Mess, MessPref) values (%s, %s, %s, %s, %s, %s)"


for i in range(1 , len(values)):
   mycursor.execute(query, (values[i][0],values[i][1],values[i][2],values[i][3],values[i][4],values[i][5]))

db.commit()

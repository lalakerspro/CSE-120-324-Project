#Basic Database
import mysql.connector

def convertFileToName(filename):
    #Converts file's name into readable data
    with open(filename, 'rb') as file:
        name = file.read()
    return name


#Insert Data
def insertDATA(date, serialnumber, image):
   # mydb = mysql.connector.connect(host='localhost',
   #                                          user='root',
    #                                         password='')
    #mycursor = mydb.cursor()
    #mycursor.execute("SHOW DATABASES")
    #for x in mycursor:
    #    if x == "python_db":
    #        print("Databse Exists...")
    #    else:   
    #        print("Creating Database...")
    #        mycursor.execute("CREATE DATABASE python_db")
    

    print("Inserting data into table.")
    try:
        #Establish Connection 
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='python_db')
        

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE infos (date VARCHAR(255), serialnumber VARCHAR(255), image VARCHAR(255))")

        #table(%s, %s, %s)
        sql = """INSERT INTO infos (date, serialnumber, image) VALUES (%s,%s,%s)"""
        val = (date, serialnumber, image)

        result = cursor.execute(sql, val)

        
        #print("Creating Database...")
        #cursor.execute("CREATE DATABASE python_db")

        #sql_insert_blob_query = """(date, serialnumber, image) VALUES (%s,%s,%s)"""

        #serialImage = "C:\\Users\\kshav\\OneDrive\\Desktop\\CSE-120-324-Project-main\\050122#spring1.png"
        #serialImage =  '5122#spring1'

        # Convert data and format
        #insert_blob_tuple = (date, serialnumber, serialImage)
        #result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        
        connection.commit()
        print("Serial # and Image inserted successfully into database")
        for x in cursor: 
            print(x)

    except mysql.connector.Error as error:
        print("Failed inserting data into table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

            #Insert Data Command Example
            #Time = Time, Day,  Month, Year
            #Serial= Serial #
            #Image = Image Name / Image
#insertDATA("19:51/4/14/22", "S158392", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG.png")
#insertDATA("20:00/4/14/22", "S603043", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG2.png")

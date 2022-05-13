#Basic Database
import mysql.connector
import numpy as np

def convertFileToName(filename):
    
    with open(filename, 'rb') as file:
        name = file.read()
    return name


#Insert Data
def insertDATA(time, legibility, imgname):

    

    print("Inserting data into table...")
    try:
        #Establish Connection
       
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root',
                                             database='python_db')
        
        cursor = connection.cursor()
        #table(%s, %s, %s)
        sql = """INSERT INTO infos (time, legibility, imgname) VALUES (%s,%s,%s)"""
        val = (time, legibility, imgname)

        result = cursor.execute(sql, val)

        
        
        
        connection.commit()
        print("Date, legibility and image inserted successfully into database")
        for x in cursor: 
            print(x)

    except mysql.connector.Error as error:
        print("Failed inserting data into table {}".format(error))

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

#Create Database Table
def createDATABASETABLE():

    print("Creating data base table...")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root',
                                             database='python_db')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE infos (time VARCHAR(255), legibility VARCHAR(255), imgname VARCHAR(255))")

        connection.commit()

    except mysql.connector.Error as error:
        print("Failed creating table in database {}".format(error))

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    

#Create Database
def createDATABASE():
    
    print("Creating Database...")
    try: 
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE python_db")
        connection.commit()
        print("Finished creating databse python_db")
    except mysql.connector.Error as error:
        print("Failed creating database in local server {}".format(error))

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

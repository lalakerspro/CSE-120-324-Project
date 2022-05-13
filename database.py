#Basic Database
import mysql.connector
import numpy as np

def convertFileToName(filename):
    
    with open(filename, 'rb') as file:
        name = file.read()
    return name


#Insert Data
def insertDATA(time, legibility, imgname):

    

    print("Inserting data into table.")
    try:
        #Establish Connection
       
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='python_db')
        

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE infos (time VARCHAR(255), legibility VARCHAR(255), imgname VARCHAR(255)")

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

#Create Database
def createDATABASE():
    connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='')
    cursor = connection.cursor()
    print("Creating Database...")
    cursor.execute("CREATE DATABASE python_db")
    connection.commit()
    done = "Finished creating databse python_db"
    return done
    
    

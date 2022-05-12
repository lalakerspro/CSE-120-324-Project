#Basic Database
import mysql.connector


def convertFileToName(filename):
    
    with open(filename, 'rb') as file:
        name = file.read()
    return name


#Insert Data
def insertDATA(time, legibility):

    

    print("Inserting data into table.")
    try:
        #Establish Connection
       
        connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='',
                                             database='python_db')
        

        cursor = connection.cursor()
        cursor.execute("CREATE TABLE infos (time VARCHAR(255), legibility VARCHAR(255), )")

        #table(%s, %s, %s)
        sql = """INSERT INTO infos (time, legibility) VALUES (%s,%s)"""
        val = (time, legibility)

        result = cursor.execute(sql, val)

        
        
        
        connection.commit()
        print("Legibility and image inserted successfully into database")
        for x in cursor: 
            print(x)

    except mysql.connector.Error as error:
        print("Failed inserting data into table {}".format(error))

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")


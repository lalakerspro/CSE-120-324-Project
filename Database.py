#Basic Database
import mysql.connector

def convertFileToName(filename):
    #Converts file's name into readable data
    with open(filename, 'rb') as file:
        name = file.read()
    return name


#Insert Data
def insertDATA(date, serialnumber, image):
    print("Inserting data into table.")
    try:
        #Establish Connection 
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='admin',
                                             password='admin')

        cursor = connection.cursor()

        sql_insert_blob_query = """(date, serialnumber, image) VALUES (%s,%s,%s)"""

        serialImage = convertFileToName(image)

        # Convert data and format
        insert_blob_tuple = (date, serialnumber, serialImage)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Serial # and Image inserted successfully into databse", result)

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
insertDATA("19:51/4/14/22", "S158392", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG.png")
insertDATA("20:00/4/14/22", "S603043", "C:\Users\Blood\source\repos\CSE-120-324-Project\IMG2.png")

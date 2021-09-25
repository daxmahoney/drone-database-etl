

# Import the required libraries:

import mysql.connector


# ---------------------------------------- CREATE THE CONNECTION WITH THE DATABASE IN AWS ---------------------------------------------

def create_connection():
    # Import the sql library:
    import mysql.connector
    
    # Create a connection
    mydb = mysql.connector.connect(
    host="drone-db.cba0wbjo4ee3.us-east-2.rds.amazonaws.com",
    user="admin",
    password="drone123!",
    database = "bcitdrone")
    
    # Show all the tables that exist in the database:
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    
    for x in mycursor:
    print(x)

    

#----------------------------------------- CREATE A TABLE AND INSERT VALUES INTO THE DATABASE--------------------------------------------


def create_table():
    mycursor = mydb.cursor()
    # Code for creating a new table:
    mycursor.execute("CREATE TABLE IMAGE_DATA (filename VARCHAR(255), GPSInfo VARCHAR(255),ResolutionUnit INT,ExifOffset INT,ImageDescription VARCHAR(225),Make VARCHAR(225),Model VARCHAR(225),Software VARCHAR(225),Orientation VARCHAR(225),DateTime DATETIME,YCbCrPositioning INT,XResolution FLOAT, YResolution FLOAT,XPComment VARCHAR(225),XPKeywords VARCHAR(225))")
    
    
# Create a function for adding all the values:

def insert_values(data_json):
    
    # Import the required JSON package:
    import json
    
    # Opening the file and loading as a dictionary:
    with open('drone_exif_data.json') as json_file:
    data = json.load(json_file)
    
    # Check the datatype of the file:
    print("Type:", type(data))
    
    # Extracting the data alone from each of the keys:
    data_values = data.values()
    data_values = list(data_values)
    
    # Loop through all the values:
    for item in data_values:
        data_one_row = item
    
        # Now parse and enter this into the table:
        placeholder = ", ".join(["%s"] * len(data_one_row))
        stmt = "insert into `{table}` ({columns}) values ({values});".format(table='IMAGE_DATA', columns=",".join(data_one_row.keys()), values=placeholder)
        mycursor.execute(stmt, list(data_one_row.values()))
        mydb.commit()
        


# View the table:


def view_tables():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM IMAGE_DATA")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)




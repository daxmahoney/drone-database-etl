#!/usr/bin/env python3

import mysql.connector
import json

USR = "admin"
PASSWORD = "drone123!"
HOST = "drone-db.cba0wbjo4ee3.us-east-2.rds.amazonaws.com"
PORT = "3306"
DBNAME = "bcitdrone"

def main():
    mydb = mysql.connector.connect(
    host=HOST,
    user=USR,
    password=PASSWORD,
        database=DBNAME
    )

    """
    example data 
    one_dict = {"stage" : "stage2", 
                "filename":"filesomewhere", 
                "filelocation":"locationoffile",
                "createdtime": "2020:04:19 14:56:47",
                "filetype":"ply"}"""

    filename = "something.json"
    with open(filename, 'r') as f:
        new_information = json.load(f)
        for information in new_information:
            insert_table(mydb, information)
            
# the downside of this approach is that you have to know the structure of the data in advance to create the values statement below
def insert_table(mydb, incoming_dict: dict):
    mycursor = mydb.cursor()
    pre_sql = "INSERT INTO drone_data_files (stage, filename, filelocation, createdtime, filetype) VALUES (%s, %s, %s, %s, %s)"
    val = (incoming_dict["stage"], incoming_dict["filename"], incoming_dict["filelocation"], incoming_dict["createdtime"], incoming_dict["filetype"])
    mycursor.execute(pre_sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")

if __name__ == "__main__":
    main()

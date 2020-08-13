#!/usr/bin/python
# -*- coding: utf-8 -*-

#change parameter on TABLE_NAME, %keyword% and change date/time to your preference. make sure commenting single querys to prevent of using them.

#!!WARNING!! be carefull with your db data, always do a backup before Use. usage of BEFORE and AFTER date can Destroy your DB if you working on a CMS like as ex. Wordpress

#written by s1ck0

import mysql.connector
from mysql.connector import Error

connection=None

#open db connection
try:
    connection = mysql.connector.connect(host='hostname',
                                         database='db-name',
                                         user='db-user',
                                         password='db-user password')

    sql_select_Query = "select * from TABLE_NAME"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in TABLE_NAME is: ", cursor.rowcount)

    print("\nPrinting each TABLE_NAME record")
    for row in records:
        print("Id = ", row[1], )
        print("post_date = ", row[3], )
        print("post_title =", row[6], )
        print("post_content = ", row[5], )
        
    cursor = connection.cursor()
    print("Deleting..")
    
    #Delete by contain TXT    
    sql_Delete_query = "DELETE FROM TABLE_NAME WHERE post_content LIKE '%keyword%'"
    cursor.execute(sql_Delete_query)
    
    #Copy the query above and add new keywords to delete with more keywords at once
    
    
    
    
    #Delete BEFORE Date
    sql_Delete_query = "DELETE FROM TABLE_NAME WHERE post_date < '2018-12-31 23:59:59'"
    cursor.execute(sql_Delete_query)
    connection.commit()
    print("Deleted..")
    
    #Delete AFTER Date
    sql_Delete_query = "DELETE FROM TABLE_NAME WHERE post_date > '2018-12-31 23:59:59'"
    cursor.execute(sql_Delete_query)
    connection.commit()
    print("Deleted..")
    
except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection:
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
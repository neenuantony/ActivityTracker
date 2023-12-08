import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor=mydb.cursor()

sql="create database activity_tracker"
mycursor.execute(sql)
print("database created successfully")
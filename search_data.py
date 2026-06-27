import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cursor = con.cursor()

name = input("Enter name to search: ")

query = "SELECT * FROM users WHERE name=%s"
cursor.execute(query, (name,))

rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No record found")

con.close()
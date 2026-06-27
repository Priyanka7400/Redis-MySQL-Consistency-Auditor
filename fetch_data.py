import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

print("Users Data:\n")

for row in rows:
    print(row)

cursor.close()
conn.close()
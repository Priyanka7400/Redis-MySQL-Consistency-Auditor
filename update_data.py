import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cursor = conn.cursor()

sql = "UPDATE users SET city = %s WHERE id = %s"
value = ("Lucknow", 100)

cursor.execute(sql, value)
conn.commit()

print(cursor.rowcount, "record updated successfully")

cursor.close()
conn.close()
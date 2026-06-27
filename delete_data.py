import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cursor = conn.cursor()

sql = "DELETE FROM users WHERE id = %s"
value = (100,)

cursor.execute(sql, value)
conn.commit()

print(cursor.rowcount, "record deleted successfully")

cursor.close()
conn.close()
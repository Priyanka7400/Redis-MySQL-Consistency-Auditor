import mysql.connector
import numpy as np

# MySQL Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cur = con.cursor()

# Read records
cur.execute("SELECT * FROM users")
mysql_records = cur.fetchall()

print("MySQL Records:", len(mysql_records))

# Simulated Redis Data (same data for now)
redis_records = mysql_records.copy()

# NumPy Comparison
mysql_array = np.array(mysql_records, dtype=object)
redis_array = np.array(redis_records, dtype=object)

matches = np.sum(mysql_array == redis_array)
total = mysql_array.size

score = (matches / total) * 100

print("Consistency Score:", round(score, 2), "%")

con.close()
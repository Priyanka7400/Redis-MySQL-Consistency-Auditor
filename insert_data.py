import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devansh@4411",
    database="auditdb"
)

cursor = conn.cursor()

cities = ["Delhi", "Mumbai", "Pune", "Indore", "Bhopal"]

for i in range(12, 101):
    name = f"User{i}"
    age = 18 + (i % 10)
    city = cities[i % len(cities)]

    cursor.execute(
        "INSERT INTO users (id, name, age, city) VALUES (%s,%s,%s,%s)",
        (i, name, age, city)
    )

conn.commit()

print("Data inserted successfully!")

cursor.close()
conn.close()
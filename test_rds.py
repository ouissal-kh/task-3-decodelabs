import mysql.connector

connection = mysql.connector.connect(
    host="decodelabs-project3-ouissal.cz6244644jgn.eu-north-1.rds.amazonaws.com",
    port=3306,
    user="admin",
    password="Qwerty123..123Q..",
    database="interns_db"
)

if connection.is_connected():
    print("✅ Connected successfully to AWS RDS!")

cursor = connection.cursor()

cursor.execute("SELECT * FROM Interns")

rows = cursor.fetchall()

print("\nInterns table:")
for row in rows:
    print(row)

cursor.close()
connection.close()

print("\n✅ Connection closed.")
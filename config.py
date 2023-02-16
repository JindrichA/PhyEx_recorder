import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="testovaci_databaze"
)
mycursor2 = mydb.cursor()
mycursor2.execute("SELECT Jmeno FROM prvni_tabulka")
myresult = mycursor2.fetchall()
lastnames = []
for row in myresult:
    for field in row:
        lastnames.append(field)

print(type(myresult))
seznam_subjektu = set(lastnames)
import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="timon1998", host="127.0.0.1", port="5432")

print("Database opened successfully")

#CREATE TABLE ATHELTE
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS ATHLETE 
      (Text_Athlete_Name TEXT       NOT NULL,
      Text_Athlete_Weight      INT    NOT NULL  );''')
print("Table created successfully")

# CREATE TABLE TRAINING
# cur = con.cursor()
# cur.execute('''CREATE TABLE TRAINING
#       (TNr INT PRIMARY KEY     NOT NULL,
#       DESIGNATION      TEXT    NOT NULL);''')
# print("Table created successfully")

con.commit()


# cur = con.cursor()

# cur.execute("INSERT INTO ATHLETE (ADMISSION,NAME,AGE,SIZE,WEIGHT,GENDER) VALUES (3, 'Jakob', '22' ,186, 80, 'Männlich')");
Name = "Lukas"
Weight = 120

cur.execute("INSERT INTO ATHLETE (Text_Athlete_Name,Text_Athlete_Weight) VALUES (%s,%s)",(Name, Weight))
con.commit()
con.close()
# con.commit()
# print("Record inserted successfully")
# con.close()
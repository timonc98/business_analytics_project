import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="timon1998", host="127.0.0.1", port="5432")

print("Database opened successfully")

# CREATE TABLE ATHELTE
# cur = con.cursor()
# cur.execute('''CREATE TABLE ATHLETE
#       (ADMISSION INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       SIZE           CHAR (50),
#       WEIGHT         CHAR(50),
#       GENDER         TEXT     NOT NULL);''')
# print("Table created successfully")

# CREATE TABLE TRAINING
cur = con.cursor()
cur.execute('''CREATE TABLE TRAINING
      (TNr INT PRIMARY KEY     NOT NULL,
      DESIGNATION      TEXT    NOT NULL);''')
print("Table created successfully")

con.commit()
con.close()

# cur = con.cursor()

# cur.execute("INSERT INTO ATHLETE (ADMISSION,NAME,AGE,SIZE,WEIGHT,GENDER) VALUES (3, 'Jakob', '22' ,186, 80, 'Männlich')");

# con.commit()
# print("Record inserted successfully")
# con.close()
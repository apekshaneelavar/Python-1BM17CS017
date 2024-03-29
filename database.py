import sqlite3

conn = sqlite3.connect('test.db')
#print ("Opened database successfully")

try:
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL,
              ADDRESS        CHAR(50),
              SALARY         REAL);''')
except sqlite3.OperationalError:
    pass
    print ("TABLE CREATED SUCCESSFULLY")
try:
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

except sqlite3.IntegrityError:
    pass

conn.commit()
print ("RECORDS CREATED SUCCESSFULLY")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
##conn.execute("UPDATE COMPANY set NAME = 'Chandu' where ID = 1")
##conn.execute("UPDATE COMPANY set NAME = 'Paul' where ID = 2")
##conn.execute("UPDATE COMPANY set NAME = 'Chandana' where ID = 3")
##conn.execute("UPDATE COMPANY set NAME = 'Minty' where ID = 4")
conn.commit()
print ("TOTAL NUMBER OF ROWS UPDATED :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("ROWS UPDATED SUCCESSFULLY\n")

conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print ("TOTAL NUMBER OF ROWS DELETED :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("ROWS DELETED SUCCESSFULLY\n")
conn.close()

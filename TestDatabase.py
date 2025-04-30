import sqlite3

'''
This SQLite comes with the python installation, so no need to download it separately
'''

conn = sqlite3.connect('test.db')
print("Opened database successfully")

# Create a cursor object
cursor = conn.cursor()

# Create the 'message' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS COMPANY (
    ID INTEGER,
    NAME TEXT,
    AGE TEXT,
    ADDRESS TEXT,
    SALARY TEXT )''')

conn.commit()

conn.execute('INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, "Paul", 32, "California", 20000.00 )')

conn.execute('INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (2, "Allen", 25, "Texas", 15000.00 )')

conn.execute('INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (3, "Teddy", 23, "Norway", 20000.00 )')

conn.execute('INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (4, "Mark", 25, "Rich-Mond", 65000.00 )')

conn.commit()
print("Records created successfully")

for row  in cursor.execute('SELECT id, name, address, salary  from COMPANY').fetchall():
    print(row)

conn.close()
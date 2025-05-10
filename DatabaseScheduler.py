import sqlite3
import schedule
import time

# Database connection
DB_PATH = 'company.db'

# Function to read data from the database
def read_data():
    global conn
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM COMPANY')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'An error occurred: {e}')
    finally:
        if conn:
            conn.close()

# Scheduler to run the read_data function every minute
#schedule.every(1).minutes.do(read_data)
schedule.every(20).seconds.do(read_data)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

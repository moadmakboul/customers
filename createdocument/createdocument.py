import sqlite3
from datetime import datetime

conn = sqlite3.connect('mydb.sqlite')
cur = conn.cursor()

def createDocument(data):
    cur.execute('''INSERT OR IGNORE INTO Customers (name, email, date_of_birth, date_of_subscription) VALUES (?,?,?,?) ''', 
                (data['name'], data['email'], data['date_of_birth'], datetime.now() ))
    conn.commit()

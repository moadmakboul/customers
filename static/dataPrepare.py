import sqlite3


class PrepareData():
    def __init__(self, data):
        self.data = data
        
    def myfunction(self):
        conn = sqlite3.connect('mydb.sqlite')
        cur = conn.cursor()

        cur.executescript('''
            DROP TABLE IF EXISTS Customers;
            CREATE TABLE Customers (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE,
                email TEXT UNIQUE,
                date_of_birth INTEGER NOT NULL,
                date_of_subscription INTEGER 
                );
            ''')
        cur.execute('''INSERT OR IGNORE INTO Customers
        (name, email, date_of_birth, date_of_subscription) VALUES ( ?, ?, ?, ?)''',
        ( self.data['name'], self.data['email'], self.data['date_of_birth'], self.data['date_of_subscription'] ) )

        conn.commit()            
            

        
        
    


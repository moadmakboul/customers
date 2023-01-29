import sqlite3


class PrepareData():
    def __init__(self, data):
        self.data = data
        
    def myfunction(self):
        conn = sqlite3.connect('mydb.sqlite')
        cur = conn.cursor()

        cur.execute('''INSERT OR IGNORE INTO Customers
        (name, email, date_of_birth, date_of_subscription) VALUES ( ?, ?, ?, ?)''',
        ( self.data['name'], self.data['email'], self.data['date_of_birth'], self.data['date_of_subscription'] ) )

        conn.commit()            
        print('created')

        
        
    


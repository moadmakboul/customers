from flask import Flask, request, render_template
from flask_cors import CORS
from createdocument import createdocument
import sqlite3

app = Flask(__name__)
cors = CORS(app)
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

@app.route('/receiver', methods=['POST'])
def RecievingData():
    data = request.get_json()
    mydocument = createdocument(data)
    return data

@app.route('/')
def RenderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)



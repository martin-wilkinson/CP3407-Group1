import sqlite3

conn = sqlite3.connect('medical.db')
statement = conn.cursor()


# if tables not created
# create tables

# create patient table
statement.execute('''CREATE TABLE IF NOT EXISTS patients
              (patient_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
              name TEXT(30)
              )''')

# create blood sugar table
statement.execute('''CREATE TABLE IF NOT EXISTS blood_sugar_history
             (time DATETIME DEFAULT CURRENT_TIMESTAMP, 
             sugar_level INTEGER, 
             patient_number INTEGER,
             FOREIGN KEY(patient_number) REFERENCES patients(patient_id)
             )''')

# create insulin table
statement.execute('''CREATE TABLE IF NOT EXISTS insulin_history
             (time DATETIME DEFAULT CURRENT_TIMESTAMP, 
             auto_state BOOLEAN,
             insulin_units INTEGER, 
             patient_number INTEGER,
             FOREIGN KEY(patient_number) REFERENCES patients(patient_id)
             )''')

# create test data table (in real-world example, this wouldn't exist)
statement.execute('''CREATE TABLE IF NOT EXISTS blood_sugar_examples
                 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 sugar_level integer
                 )''')

# save changes
conn.commit()

# close connection
conn.close()
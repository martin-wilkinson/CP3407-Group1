import sqlite3


def create_tables():

    conn = sqlite3.connect('medical.db')
    c = conn.cursor()

    # create patient table
    # c.execute('''CREATE TABLE IF NOT EXISTS patients
    #              (patient_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #               patient_name TEXT(30)
    #              )''')

    # c.executescript('''DROP TABLE IF EXISTS blood_sugar_history''')
    # c.executescript('''DROP TABLE IF EXISTS insulin_history''')

    # create blood sugar table
    c.execute('''CREATE TABLE IF NOT EXISTS blood_sugar_history
                 (blood_sugar_recorded_time DATETIME DEFAULT CURRENT_TIMESTAMP, 
                  sugar_level INTEGER 
                 )''')

    # create insulin table
    c.execute('''CREATE TABLE IF NOT EXISTS insulin_history
            (insulin_recorded_time DATETIME DEFAULT CURRENT_TIMESTAMP, 
                  auto_state BOOLEAN,
                  insulin_units INTEGER
                 )''')

    conn.commit()
    conn.close()


# def add_to_patient_table(*args):
#
#     conn = sqlite3.connect('medical.db')
#     c = conn.cursor()
#
#     c.executemany('INSERT INTO patients VALUES (NULL, ?)', *args)
#
#     conn.commit()
#     conn.close()


def add_to_blood_sugar_table(sugar_level):

    conn = sqlite3.connect('medical.db')
    c = conn.cursor()

    c.execute('INSERT INTO blood_sugar_history VALUES (NULL, ?)', (sugar_level,))

    conn.commit()
    conn.close()


def add_to_insulin_history(insulin_state, insulin_units):

    conn = sqlite3.connect('medical.db')
    c = conn.cursor()

    c.execute('INSERT INTO insulin_history VALUES (NULL, ?, ?)', (insulin_state, insulin_units))

    conn.commit()
    conn.close()


# def pull_from_patient_table(entered_id):
#
#     conn = sqlite3.connect('medical.db')
#     c = conn.cursor()
#
#     patient_data = c.execute('SELECT patient_id FROM patient WHERE patient_id = "' + entered_id + '"')
#     conn.commit()
#     conn.close()
#     return patient_data


# def pull_from_blood_sugar_table():
#
#     conn = sqlite3.connect('medical.db')
#     c = conn.cursor()
#
#     c.execute('SELECT blood_sugar_recorded_time FROM blood_sugar_history')
#     blood_sugar_data = c.fetchmany(3)
#     conn.commit()
#     conn.close()
#     return blood_sugar_data
#
#
# def pull_from_insulin_history():
#
#     conn = sqlite3.connect('medical.db')
#     c = conn.cursor()
#
#     c.execute('SELECT insulin_recorded_time FROM insulin_history')
#     insulin_data = c.fetchmany(3)
#     conn.commit()
#     conn.close()
#     return insulin_data

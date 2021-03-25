import sqlite3
from sqlite3 import Error
from datetime import date
import sys

try:
    # Intenta hacer la conexión
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS habits(habit_id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, action TEXT NOT NULL, measurement TEXT NOT NULL, days TEXT NOT NULL, cycle_date TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS tracking(habit_id INTEGER NOT NULL, day INTEGER NOT NULL, status TEXT NOT NULL, PRIMARY KEY(habit_id, day), FOREIGN KEY(habit_id) REFERENCES habits(habit_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS setbacks(setback_id INTEGER NOT NULL PRIMARY KEY, day INTEGER NOT NULL, description TEXT NOT NULL, cycle_date TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS reviews(review_id INTEGER NOT NULL PRIMARY KEY, description TEXT NOT NULL, cycle_date TEXT NOT NULL);")

    con.commit()

    def close_connection():
        con.close()


    def get_cycle_date():
        current_date = date.today()
        cycle_date = date(current_date.year, current_date.month, 1 if current_date.day < 16 else 16)
        return cycle_date
        

    def current_cycle_exists():
        cycle_date = get_cycle_date()
        cur.execute("SELECT * FROM habits WHERE cycle_date = ?", (cycle_date,))
        cycle = cur.fetchone()

        return cycle != None

    
    def add_new_habit(habits):
        cur.executemany("INSERT INTO habits(name, action, measurement, days, cycle_date) VALUES(?, ?, ?, ?, ?)", habits)
        con.commit()


except Error:
    # En caso de error
    print(Error)
    con.close()
    sys.exit()




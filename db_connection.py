import sqlite3
from sqlite3 import Error
from datetime import date
import sys

try:
    # Intenta hacer la conexión
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS cycles(cycle_id INTEGER NOT NULL PRIMARY KEY, initial_date TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS habits(habit_id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, action TEXT NOT NULL, measurement TEXT NOT NULL, days TEXT NOT NULL, cycle_id INTEGER NOT NULL, FOREIGN KEY(cycle_id) REFERENCES cycles(cycle_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS tracking(habit_id INTEGER NOT NULL, day INTEGER NOT NULL, status TEXT NOT NULL, PRIMARY KEY(habit_id, day), FOREIGN KEY(habit_id) REFERENCES habits(habit_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS setbacks(setback_id INTEGER NOT NULL PRIMARY KEY, day INTEGER NOT NULL, description TEXT NOT NULL, cycle_id INTEGER NOT NULL, FOREIGN KEY(cycle_id) REFERENCES cycles(cycle_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS reviews(review_id INTEGER NOT NULL PRIMARY KEY, description TEXT NOT NULL, cycle_id INTEGER NOT NULL, FOREIGN KEY(cycle_id) REFERENCES cycles(cycle_id) ON DELETE CASCADE);")

    con.commit()

    def close_connection():
        con.close()


    def get_initial_date():
        current_date = date.today()
        initial_date = date(current_date.year, current_date.month, 1 if current_date.day < 16 else 16)
        return initial_date
        

    def current_cycle_exists():
        initial_date = get_initial_date()
        cur.execute("SELECT * FROM cycles WHERE initial_date = ?", (initial_date,))
        cycle = cur.fetchone()

        return cycle != None


except Error:
    # En caso de error
    print(Error)
    con.close()
    sys.exit()




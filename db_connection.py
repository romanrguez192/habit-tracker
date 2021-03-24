import sqlite3
from sqlite3 import Error

try:
    # Intenta hacer la conexión
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS cycles(cycle_id INTEGER NOT NULL PRIMARY KEY, initial_date TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS habits(habit_id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, action TEXT NOT NULL, measurement TEXT NOT NULL, days TEXT NOT NULL, cycle_id INTEGER NOT NULL, FOREIGN KEY(cycle_id) REFERENCES cycles(cycle_id) ON DELETE CASCADE);")
    cur.execute("CREATE TABLE IF NOT EXISTS tracking(habit_id INTEGER NOT NULL, day INTEGER NOT NULL, status TEXT NOT NULL, PRIMARY KEY(habit_id, day), FOREIGN KEY(habit_id) REFERENCES habits(habit_id) ON DELETE CASCADE);")

    con.commit()

except Error:
    # En caso de error
    print(Error)

finally:
    # Cierra la conexión
    con.close()



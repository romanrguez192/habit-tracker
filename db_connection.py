import sqlite3
from sqlite3 import Error
import utils
import sys
from languages import dates

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
        

    def current_cycle_exists():
        cycle_date = utils.get_cycle_date()
        cur.execute("SELECT * FROM habits WHERE cycle_date = ?", (cycle_date,))
        cycle = cur.fetchone()

        return cycle != None

    
    def add_new_habit(habits):
        cur.executemany("INSERT INTO habits(name, action, measurement, days, cycle_date) VALUES(?, ?, ?, ?, ?)", habits)
        con.commit()

    def get_habits(cycle_date, lang):

        habits = []
        cur.execute("""
            SELECT h.habit_id, h.name, h.action, h.measurement, h.days, t.day, t.status
            FROM habits AS h
            LEFT JOIN tracking AS t
            ON h.habit_id = t.habit_id
            WHERE cycle_date = ?
            ORDER BY h.habit_id, t.day;
        """, (cycle_date,))
        
        habits_list = cur.fetchall()

        habit = {}
        habit["id"] = habits_list[0][0]
        habit["name"] = habits_list[0][1]
        habit["action"] = habits_list[0][2]
        habit["measurement"] = habits_list[0][3]
        habit["days"] = habits_list[0][4]
        habit["days"] = list(map(int , habit["days"].split()))
        habit["days_str"] = " ".join(map(lambda d: dates[lang]["days"][d] , habit["days"]))
        habit["tracking"] = {habits_list[0][5]: habits_list[0][6]}
        habits.append(habit)

        for i in range(1, len(habits_list)):
            if habits_list[i][0] != habits_list[i - 1][0]:
                habit = {}
                habit["id"] = habits_list[0][0]
                habit["name"] = habits_list[i][1]
                habit["action"] = habits_list[i][2]
                habit["measurement"] = habits_list[i][3]
                habit["days"] = habits_list[i][4]
                habit["days"] = list(map(int , habit["days"].split()))
                habit["days_str"] = " ".join(map(lambda d: dates[lang]["days"][d] , habit["days"]))
                habit["tracking"] = {habits_list[i][5]: habits_list[i][6]}
                habits.append(habit)
            else:
                habit["tracking"][habits_list[i][5]] = habits_list[i][6]

        return habits


except Error:
    # En caso de error
    print(Error)
    con.close()
    sys.exit()




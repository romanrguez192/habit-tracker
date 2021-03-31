from languages import messages, dates
import db_connection as db
from calendar import monthrange
import utils

# Selección del idioma de la aplicación
def select_language():
    lang = ""
    LANGUAGES = messages.keys()
    try:
        # Intenta abrir el archivo
        with open("lang.txt", "r") as f:
            lang = f.read(2).upper()
            # Si no es un idioma válido
            if lang not in LANGUAGES:
                raise FileNotFoundError

    # En caso de error, se solicita el idioma
    except FileNotFoundError:
        while lang not in LANGUAGES:
            for lang_messages in messages.values():
                print(lang_messages["choose"])
            lang = input(">>> ").upper()
        
        # Escribe en el archivo
        with open("lang.txt", "w") as f:
            f.write(lang)

    # En ambos casos devuelve el idioma
    return lang


# Generalización de funciones de menús
def menu(options, functions):
    option = ""
    while option != str(len(options)):
        option = ""
        while option not in map(str, range(1, len(options) + 1)):
            print()
            for n, opt in enumerate(options):
                print(f"{n + 1}. {messages[opt]}")
            
            option = input(">>> ")

        for n, function in enumerate(functions):
            if option == str(n + 1):
                function()
                break


# Menú principal
def main_menu():
    menu(("current_cycle", "past_cycles", "exit"), (current_cycle_menu, past_cycles_menu))


# Encabezado con todos los hábitos y su seguimiento
def print_habits():
    cycle_date = utils.get_cycle_date()
    d, m, y = cycle_date.day, cycle_date.month, cycle_date.year

    print()
    print(messages["heading_date"](d, m, y))

    habits = db.get_habits(cycle_date, lang)
    month_days = monthrange(y, m)

    first_day = d
    last_day = 15 if first_day == 1 else month_days[1]

    num_days = last_day - first_day + 1
    first_day_week = month_days[0] if first_day == 1 else month_days[0] + 15

    for i, habit in enumerate(habits):
        print()
        print(f"{i + 1}) {habit['name']}: {habit['action']}. {habit['measurement']}. {habit['days_str']}")
        for j in range(num_days):
            print(dates[lang]["days"][(first_day_week + j) % 7], end=" ")
        print()
        for j in range(first_day, last_day + 1):
            print(("0" if j < 10 else "") + str(j), end=" ")
        print()
        for j, k in zip(range(num_days), range(first_day, last_day + 1)):
            if (first_day_week + j) % 7 in habit["days"]:
                if k in habit["tracking"]:
                    print(habit["tracking"][k] * 2, end=" ")
                else:
                    print("__", end=" ")
            else:
                print("   ", end="")
        print()


# Menú de opciones del ciclo actual
def current_cycle_menu():
    while not db.current_cycle_exists():
        new_cycle()
    
    print_habits()
        
    menu(("mark_habits", "setback_notes", "cycle_review", "back"), (mark_habits, setback_notes, reviews))


# Menú para marcar el seguimiento de los hábitos
def mark_habits():
    print()
    cycle_date = utils.get_cycle_date()
    d, m, y = cycle_date.day, cycle_date.month, cycle_date.year

    month_days = monthrange(y, m)
    first_day = d
    last_day = 15 if first_day == 1 else month_days[1]
    first_day_week = month_days[0] if first_day == 1 else (month_days[0] + 15) % 7
    num_days = last_day - first_day + 1

    habits = db.get_habits(cycle_date, lang)

    number = ""
    while number not in map(str, range(1, len(habits) + 1)) :
        number = input("- " + messages["habit_number"] + ": ")
    number = int(number)

    week_days = habits[number - 1]["days"]

    possible_days = [i + first_day for i in range(num_days) if (first_day_week + i) % 7 in week_days]

    day = ""
    while day not in map(str, possible_days):
        day = input("- " + messages["day_mark"] + ": ")
    day = int(day)

    symbol = ""
    while symbol not in ("+", "-", "*"):
        symbol = input("- " + messages["symbol"] + ": ")

    habit_id = habits[number - 1]["id"]

    db.mark_habit(habit_id, day, symbol)
    print()
    print(messages["marked"])
    print_habits()


# Menú para agregar las notas de los retrasos y para listarlas
def setback_notes():
    cycle_date = utils.get_cycle_date()
    notes = db.get_setback_notes(cycle_date)
    print()

    if len(notes) == 0:
        print(messages["no_setbacks"])

    for note in notes:
        print(f"{note['day']}: {note['description']}")
    
    ans = ""
    while ans != messages["no"]:
        print()
        ans = ""
        while ans not in (messages["yes"], messages["no"]):
            print(f"{messages['add_setback']} ({messages['yes']}/{messages['no']})")
            ans = input(">>> ").upper()

        if ans == messages["yes"]:
            day = input("- " + messages["setback_day"] + ": ")
            note = input("- " + messages["write_setback"] + ": " )
            db.add_setback(cycle_date, day, note)
    
    print_habits()
    

# Menú para agregar las revisiones de los ciclos y para listarlas
def reviews():
    cycle_date = utils.get_cycle_date()
    reviews = db.get_reviews(cycle_date)
    print()

    if len(reviews) == 0:
        print(messages["no_reviews"])

    for i, review in enumerate(reviews):
        print(f"{i + 1}. {review}")
    
    ans = ""
    while ans != messages["no"]:
        print()
        ans = ""
        while ans not in (messages["yes"], messages["no"]):
            print(f"{messages['add_review']} ({messages['yes']}/{messages['no']})")
            ans = input(">>> ").upper()

        if ans == messages["yes"]:
            comment = input("- " + messages["write_review"] + ": " )
            db.add_review(cycle_date, comment)
    
    print_habits()


# Creación de nuevo ciclo
def new_cycle():
    cycle_date = utils.get_cycle_date()
    d, m, y = cycle_date.day, cycle_date.month, cycle_date.year
    print()
    print(messages["new_start_date"](d, m, y))
    print()
    print(messages["add_new_habit"] + ":")

    habits = []
    ans = ""
    while ans != messages["no"]:
        name = input("- " + messages["habit_name"] + ": ")
        action = input("- " + messages["habit_action"] + ": ")
        measurement = input("- " + messages["habit_measurement"] + ": ")
        
        days = ""
        while not utils.valid_habit_days(days, lang):
            days = input("- " + messages["habit_days"] + ": ")
        days = utils.get_list_days(days, lang)
        print()

        habits.append((name, action, measurement, days, cycle_date))

        ans = ""
        while ans not in (messages["yes"], messages["no"]):
            print(f"{messages['ask_new_habit']} ({messages['yes']}/{messages['no']})")
            ans = input(">>> ").upper()
        print()
    
    db.add_new_habit(habits)
    print(messages["cycle_created"])


# Menú de ciclos anteriores
def past_cycles_menu(): 
    option = ""
    while option != "2":
        option = ""
        while option not in map(str, range(1, 2 + 1)):
            print()
            print("1.", messages["new_cycle"])
            print("2.", messages["back"])
            option = input(">>> ")
            
        if  option == "1":
            print("XD")


# Selección de idioma
lang = select_language()
# Bienvenida a la aplicación
messages = messages[lang]
print(messages["welcome"])
# Menú principal
main_menu()
db.close_connection()
from languages import messages
import db_connection as db

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


# Menú de opciones del ciclo actual
def current_cycle_menu():
    while not db.current_cycle_exists():
        new_cycle()
    
    print()
    print("Equis fecha xd")


# Creación de nuevo ciclo
def new_cycle():
    cycle_date = db.get_cycle_date()
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
        days = input("- " + messages["habit_days"] + ": ")
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
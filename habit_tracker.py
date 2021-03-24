from messages import messages
import db_connection

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

# Menú principal
def main_menu():
    option = ""
    while option != "3":
        option = ""
        while option not in map(str, range(1, 3 + 1)):
            print()
            print("1.", messages["current_cycle"])
            print("2.", messages["past_cycles"])
            print("3.", messages["exit"])
            option = input(">>> ")

        if option == "1":
            current_cycle_menu()
        elif option == "2":
            past_cycles_menu()


# Menú de opciones del ciclo actual
def current_cycle_menu(): 
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
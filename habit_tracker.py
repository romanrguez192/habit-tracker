from messages import messages

LANGUAGES = messages.keys()
lang = ""

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

# Bienvenida a la aplicación
messages = messages[lang]
print(messages["welcome"])

# Menú de opciones
option = ""
while option not in map(str, [i + 1 for i in range(3)]):
    print(messages["current_cycle"])
    print(messages["past_cycles"])
    print(messages["exit"])
    option = input(">>> ")



from messages import messages

LANGUAGES = messages.keys()
lang = ""

try:
    with open("lang.txt", "r") as f:
        lang = f.read(2).upper()
        if lang not in LANGUAGES:
            raise FileNotFoundError

except FileNotFoundError:
    while lang not in LANGUAGES:
        for lang_messages in messages.values():
            print(lang_messages["choose"])
        lang = input(">>> ").upper()
    
    with open("lang.txt", "w") as f:
        f.write(lang)

messages = messages[lang]
print(messages["welcome"])


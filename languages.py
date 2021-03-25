dates = {
    "EN": {
        "months": (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ),
        "days": (
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        )
    },
    "ES": {
        "months": (
            "Enero",
            "Febrero",
            "Marzo",
            "Abril",
            "Mayo",
            "Junio",
            "Julio",
            "Agosto",
            "Septiembre",
            "Octubre",
            "Noviembre",
            "Diciembre"
        ),
        "days": (
            "Lunes",
            "Martes",
            "Miércoles",
            "Jueves",
            "Viernes",
            "Sábado",
            "Domingo"
        )
    },
}

messages = {
    "EN": {
        "choose": "What language do you speak? (EN)",
        "welcome": "Welcome!",
        "current_cycle": "Current cycle",
        "past_cycles": "Past cycles",
        "exit": "Exit",
        "new_cycle": "Start new cycle",
        "back": "Go back",
        "new_start_date": lambda d, m, y: "This cycle starts on {} {}, {}".format(dates["EN"]["months"][m-1], d, y),
    },
    "ES": {
        "choose": "¿Qué idioma hablas? (ES)",
        "welcome": "¡Bienvenido!",
        "current_cycle": "Ciclo actual",
        "past_cycles": "Ciclos anteriores",
        "exit": "Salir",
        "new_cycle": "Iniciar nuevo ciclo",
        "back": "Retroceder",
        "new_start_date": lambda d, m, y: "Este ciclo inicia el {} de {} de {}".format(d, dates["ES"]["months"][m-1], y),
    }
}

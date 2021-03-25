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
        "back": "Go back",
        "new_start_date": lambda d, m, y: f"This cycle has started on {dates['EN']['months'][m-1]} {d}, {y}",
        "add_new_habit": "Add a new habit",
        "habit_name": "Habit name",
        "habit_action": "Action",
        "habit_measurement": "Measurement/quantity/time",
        "habit_days": "Days of the week",
        "ask_new_habit": "Add another habit?",
        "yes": "Y",
        "no": "N",
        "cycle_created": "Cycle successfully created",
    },
    "ES": {
        "choose": "¿Qué idioma hablas? (ES)",
        "welcome": "¡Bienvenido!",
        "current_cycle": "Ciclo actual",
        "past_cycles": "Ciclos anteriores",
        "exit": "Salir",
        "back": "Retroceder",
        "new_start_date": lambda d, m, y: f"Este ciclo ha iniciado el {d} de {dates['ES']['months'][m-1]} de {y}",
        "add_new_habit": "Agrega un hábito nuevo",
        "habit_name": "Nombre del hábito",
        "habit_action": "Acción",
        "habit_measurement": "Medida/cantidad/tiempo",
        "habit_days": "Días de la semana",
        "ask_new_habit": "¿Agregar otro hábito?",
        "yes": "S",
        "no": "N",  
        "cycle_created": "Ciclo creado exitosamente",
    }
}

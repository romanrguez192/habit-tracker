from datetime import date
 
def get_cycle_date():
    current_date = date.today()
    cycle_date = date(current_date.year, current_date.month, 1 if current_date.day < 16 else 16)
    return cycle_date
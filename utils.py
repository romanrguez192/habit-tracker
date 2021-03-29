from datetime import date
from languages import dates

def get_cycle_date():
    current_date = date.today()
    cycle_date = date(current_date.year, current_date.month, 1 if current_date.day < 16 else 16)
    return cycle_date


def valid_habit_days(days, lang):
    days = days.lower()
    week = [day.lower() for day in dates[lang]["days"]]

    if days == "":
        return False

    if days == dates[lang]["daily"]:
        return True
    
    days = days.split()
    last = -1

    for portion in days:
        if "-" in portion:
            portion = portion.split("-")
            if len(portion) != 2:
                return False
            if portion[0] not in week or portion[1] not in week:
                return False
            if week.index(portion[0]) >= week.index(portion[1]):
                return False
            if week.index(portion[0]) > last:
                last = week.index(portion[1])
            else:
                return False 
        elif portion in week and week.index(portion) > last:
            last = week.index(portion)
        else:
            return False

    return True


def get_list_days(days, lang):
    days = days.lower()
    week = [day.lower() for day in dates[lang]["days"]]

    if days == "d":
        return "0 1 2 3 4 5 6"
    
    days = days.split()
    days_list = ""

    for portion in days:
        if "-" in portion:
            portion = portion.split("-")
            for i in range(week.index(portion[0]), week.index(portion[1]) + 1):
                days_list += str(i) + " "
        else:
            days_list += str(week.index(portion)) + " "

    return days_list.strip()
    

    

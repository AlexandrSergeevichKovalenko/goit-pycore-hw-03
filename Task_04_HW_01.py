from datetime import date, datetime, timedelta

# function converts string to datetime obj
def string_to_date(date_string:str):
    datetime_object = datetime.strptime(date_string, "%Y.%m.%d").date()
    return datetime_object

# function converts datetime obj to string 
def date_to_string(date):
    str_data = date.strftime("%Y.%m.%d")
    return str_data

# function to return a list of users where the 
def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

# searching for the next day of the next week from some start date 
def find_next_weekday(start_date, weekday):
    day_of_week_start_day = start_date.weekday()
    days_ahead = (weekday - day_of_week_start_day) if (weekday - day_of_week_start_day) > 0 else (weekday - day_of_week_start_day) + 7
    weekday_new = timedelta(days = days_ahead) + start_date
    return weekday_new

# if birthday is on the weekend shift the congratulation date to the next monday
def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday,0)
    
    return birthday

# final function
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year + 1)    

        if 0 <= (birthday_this_year - today).days <= days:
            congratulation_date = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(congratulation_date)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.03.08"},
    {"name": "Jane Smith", "birthday": "1990.03.5"},
    {"name": "John Depp", "birthday": "1985.01.23"},
    {"name": "Janifer Lopes", "birthday": "1990.01.27"}
]

print(get_upcoming_birthdays(prepare_user_list(users)))



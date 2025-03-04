from datetime import datetime

def get_days_from_today(date:str):
    try:
        #getting the current date and time
        now = datetime.now()
        # convert str object in datetime object
        date_datetime_obj = datetime.strptime(date,"%Y-%m-%d")
        #difference between dates
        delta  = date_datetime_obj - now
        #return the result in days
        return delta.days
    except ValueError:
        return "The inputed data format is incorrect. Please enter the data in YYYY-MM-DD format"


#calling function get_days_from_today and asking to enter the data continiously untill get the correct responce
while True:
    res = get_days_from_today(input("Enter the data in YYYY-MM-DD format:"))
    if type(res) != str: 
        print(f"Difference between today and inputted data is {res} days")
        break
        






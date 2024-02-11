import datetime as dt
from datetime import datetime as dtdt

date = input("Enter the date in YYYY-MM-DD format: ")

def get_days_from_today(date):
    try:
        userDate = dtdt.strptime(date, "%Y-%m-%d").date()
        currentDate = dtdt.today().date()
        difference = (currentDate - userDate)
        return difference.days
    except Exception:
        print("The date entered does not match the format YYYY-MM-DD")

get_days_from_today(date)
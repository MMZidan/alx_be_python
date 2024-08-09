from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    display_current_datetime= datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {display_current_datetime}")

def calculate_future_date():
        display_current_datetime= datetime.now()
        days=int(input("Enter the number of days to add to the current date: "))
        future_date=timedelta(days)+display_current_datetime
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
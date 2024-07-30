from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    display_current_datetime= datetime.now()
    print(f"Current date and time: {display_current_datetime}")

def calculate_future_date():
        display_current_datetime= datetime.now()
        days=int(input("Enter the number of days to add to the current date: "))
        future_date=timedelta(days)+display_current_datetime
        print(future_date.date())

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
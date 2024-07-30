from datetime import datetime
from datetime import timedelta

display_current_datetime = datetime.now()
print(f"Current date and time: {display_current_datetime}")


def calculate_future_date():
    days=int(input("Enter the number of days to add to the current date: "))
    future_date=timedelta(days)+display_current_datetime
    print(future_date.date())

if __name__ == "__main__":
    calculate_future_date()
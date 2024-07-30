import datetime

display_current_datetime = datetime.datetime.now()
print(f"Current date and time: {display_current_datetime}")

print(display_current_datetime.strftime("%j"))


def calculate_future_date():
    days=int(input("Enter the number of days to add to the current date: "))
    future_date=datetime.timedelta(days)+display_current_datetime
    print(future_date)

if __name__ == "__main__":
    calculate_future_date()
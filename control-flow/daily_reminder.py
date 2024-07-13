task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

def reminder(priority):
    match priority:
        case "high": print (f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        case "medium":  print (f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        case "low":  print (f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        case _: print("Please enter a valid value for your task priority (high/medium/low)") 
print(time_bound)
if time_bound=="yes":
    reminder(priority)
else :
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
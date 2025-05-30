task=input("Enter your task:")
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task. Try to complete it soon."
    case "low":
        reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
print(f"Reminder: {reminder}")        
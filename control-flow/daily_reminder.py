task=input("Enter your task:")
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")
if time_bound == "no":
    match priority:
        case "high":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
        case "medium":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
        case "low":
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
else:            
    match priority:
        case "high":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        case "medium":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        case "low":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")


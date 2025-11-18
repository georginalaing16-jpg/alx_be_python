# Prompt User to enter a task description
Task = input("Enter your task: ")
# Prompt User for task priority
Priority = input("Priority (high/medium/low): ")
# Ask if task is time-bound
Time_bound = input("Is it time-bound? (yes/no): ")
# Process task based on priority ans sensitivity
match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{Task}' is a high priority task. Please address it soon.")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a medium priority task that should be completed on time.")
        else:
            print(f"Reminder: '{Task}' is a medium priority task. Try to complete it when possible.")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a low priority task but has a deadline. Don't forget to complete it.")
        else:
            print(f"Reminder: '{Task}' is a low priority task. You can do it at your leisure.")

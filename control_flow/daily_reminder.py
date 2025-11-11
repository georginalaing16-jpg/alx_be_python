# Prompt User to enter a task description
task = input("Enter your task: ")
# Prompt User for task priority
priority = input("Priority (high, medium, low): ")
# Ask if task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")
# Process task based on priority ans sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that needs immediate attention!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed on time.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to complete it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but has a deadline. Don't forget to complete it.")
        else:
            print(f"Reminder: '{task}' is a low priority task. You can do it at your leisure.")

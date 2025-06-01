task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

match priority:
    case "high":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {task} is high priority schedule a date to finish")

    case "medium":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a medium priority task that requires to be finish before deadline!")
        else:
            print(f"Reminder: {task} is medium priority task, schedule a date to finish")

    case "low":
        if time_bound == "yes":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

        else:
            time_bound == "no"
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

def display_current_datetime():
    from datetime import datetime
    datetime = datetime.now()
    # Format datetime display
    format_datetime = datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", format_datetime)

# Prompt User to enter number of days
number_of_days = int(input("Enter number of days to add to the current date: "))
def calculate_future_date():
    from datetime import datetime, timedelta
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    #Format future date display
    formatted_future_date = future_date.strftime("%Y-%M-%d")
    print("Future date:", formatted_future_date)

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

# importing external libraries
from datetime import datetime, timedelta

# Dispaly the current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.srftime("%Y-%m-%d %H:%M:%S"))

# Calculating future date
def calculate_future_date():
    days_increase = input("Enter the number of days to add to the current date: ")
    if days_increase.isdigit():
        days_to_add = int(days_increase)
        future_date = datetime.now() + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))

    else:
        print("Invalid input. Please enter a positive integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

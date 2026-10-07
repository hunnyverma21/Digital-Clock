from datetime import datetime

print("===== DAY OF THE DATE FINDER =====")

date_input = input("Enter date (DD-MM-YYYY): ")

try:
    date = datetime.strptime(date_input, "%d-%m-%Y")
    day = date.strftime("%A")

    print(f"\nDate: {date_input}")
    print(f"Day: {day}")

except ValueError:
    print("\nInvalid date format!")
    print("Please enter the date in DD-MM-YYYY format.")
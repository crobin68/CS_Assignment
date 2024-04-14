def user_date():
    while True:
        year = input("Please enter a Year : ")
        if year.isdigit() and int(year) > 2023 and int(year) < 9999:
            break
        print("Please enter a valid number between 2024 and 9999.")

    while True:
        month = input("Please enter the month number: ")
        if month.isdigit() and 1 <= int(month) <= 12:
            break
        print("Please enter a valid month number between 1 and 12.")

    while True:
        day = input("Please enter a Day number: ")
        if day.isdigit() and 1 <= int(day) <= 31:
            break
        print("Please enter a valid day number between 1 and 31.")

    date = f"{year}-{month}-{day}"
    return date

date = user_date()
print("You entered:", date)

def user_date():
    while True:
        year = input("Please enter a Year: ")
        if year.isdigit() and 2023 < int(year) < 9999:
            break
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\033[1;31m Please enter a valid number between 2024 and 9999. \033[0m")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    while True:
        month = input("Please enter the month number: ")
        if month.isdigit() and 1 <= int(month) <= 12:
            break
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\033[1;31m Please enter a valid month number between 1 and 12. \033[0m")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    # Define the function to get the day outside the loop
    def loop_day():
        while True:
            day_input = input("Please enter a Day number: ")
            if day_input.isdigit() and 1 <= int(day_input) <= 31:
                return int(day_input)
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid day number between 1 and 31. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    # Call the function to get the day
    day = loop_day()

    # Check if the month has 30 days
    if int(month) in [2, 4, 6, 9, 11] and day > 30:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\033[1;31m This month has only 30 days. Please enter a valid day. \033[0m")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        day = loop_day()  # Call the function again to get a valid day

    date = f"{year}-{month}-{day}"  # Format the date
    return date

date = user_date()
print(date)

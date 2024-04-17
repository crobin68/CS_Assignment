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
        return month

    



    """
    get input form user 
    IF
    day is a number 
    and
    day is greater then or = to 1
    and less then or = to 31
    output the

    
    """
    
    def loop_day():
        while True:
            day_input = input("Please enter a Day number: ")
            if day_input.isdigit() and 1 <= int(day_input) <= 31:   #checking for number betwee 1-31
                return int(day_input)       # to get the var outside the (loop_day)
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid day number between 1 and 31. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    # Calling the function to get (day) inside the loop
    day = loop_day()





    """

    IF the (month) input for user is (2 , 4 , 6 , 9 , 11) 
    AND
    If the (day) input is Greater then 30
    THEN
    Tell user that month has only 30 days

    """

    if int(month) in [2, 4, 6, 9, 11] and day > 30: #months 2,4,6,9,11 only have 30 days in the month
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\033[1;31m This month has only 30 days. Please enter a valid day. \033[0m")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        day = loop_day()  # Call the function again to get a valid day

    date = f"{year}-{month}-{day}"  # Format the date
    
    return date, int(month)


date, month = user_date()


def word_month():
    word_month = ["January","Febuary","March","April","May","June","July","Augest","September","October","November","December"]

    list_month = str([word_month[month-1]])[2:-2]
    print(f"the month you selected is {list_month}")
    return list_month



print(f"The date you entered {word_month()} {date}")
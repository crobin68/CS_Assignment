import time

events = []
# welcome message 
def welcome_message():
    print("Welcome to your event planner")


# this is to add the event from the users input
def add_event():
    # prompts the user to make the format for the date portion
    def user_date():
        while True:
            year = input("Please enter a Year : ")
            if year.isdigit() and int(year) > 2023 and int(year) < 9999: # to make sure the year is withen 2023 and 9999
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                # if the number is not valid prompt this message
            print("\033[1;31m Please enter a valid number between 2024 and 9999. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        while True:
            month = input("Please enter the month number: ")
            if month.isdigit() and 1 <= int(month) <= 12:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                # if the number is not valid prompt this message
            print("\033[1;31m Please enter a valid month number between 1 and 12. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        while True:
            day = input("Please enter a Day number: ")
            if day.isdigit() and 1 <= int(day) <= 31:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                # if the number is not valid prompt this message
            print("\033[1;31m Please enter a valid day number between 1 and 31. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        date = (f"{year}-{month}-{day}") # set the format of the date 
        return date

    title = input("Enter an Event Title = ")
    date = user_date() # grab the date var 
    attendees = input("Enter event attendees (comma-separated): ").split(',') # when the user puts a "," in-between the people is formats is like a list
    events.append({"Title": title, "Date": date, "Attendees": attendees}) # when the user creates an event it uses this empty libery
    print("You have added an event to your list")


# if there are no events this message displays 
def view_events():
    if not events:
        print("No upcoming events.") 
        return
    print("Upcoming events:") 
    for index, event in enumerate(events, start=1):
        print(f"{index}.) {event['Title']} - {event['Date']}")


def view_event_details():
    view_events()   # call the code block (view_events)
    event_index = input("Select an event to view details (enter the event number): ") # select an event that you want to view
    try:
        event_index = int(event_index)
        if 1 <= event_index <= len(events):
            event = events[event_index - 1]
            print("========================================")
            print("Event Details:")
            print(f"Title: {event['Title']}")
            print(f"Date: {event['Date']}")
            print("Attendees:")
            for attendee in event['Attendees']:
                print(f"- {attendee}")
            print("========================================")
        else:
            print("Invalid event number. Please enter a valid event number.") # if the user inputs a number that is not there send user to menu
    except ValueError:
        print("Invalid input. Please enter a valid event number.")


def event_planner():
    welcome_message() # send the welcome message 
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Please select an option")
        print("1) Add an event")
        print("2) View upcoming events")
        option = input("Please choose an option: ")

        if option == '1': # if user input is ('1') then execute the block (add_event)
            add_event()
        elif option == '2': # if user input is ('1') then execute the block (view_event_details)
            view_event_details()
        else:
            print("------------------------------------------------")
            print("Unknown option. Please select between 1 and 2")
            print("------------------------------------------------")


event_planner() # execute the whole code on screen

import time

# define a empty libery 
events = []


# wleocme the user with a message
def welcome_message():
    print("Welcome to your event planner")




# when option 2 is selected from (event_planner)
def add_event():

    def user_date():#to make sure the user makes the correct format when putting in the date
        while True:
            year = input("Please enter a Year : ")      # get the input for the year
            if year.isdigit() and int(year) > 2023 and int(year) < 9999:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid number between 2024 and 9999. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        while True:
            month = input("Please enter the month number: ")    #get the input for the month
            if month.isdigit() and 1 <= int(month) <= 12:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid month number between 1 and 12. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        while True:
            day = input("Please enter a Day number: ")      #get the input for the day
            if day.isdigit() and 1 <= int(day) <= 31:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid day number between 1 and 31. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        date = (f"{year}-{month}-{day}")    #format all the dates into one variable
        return date


    title = input("Enter an Event Title = ")
    date = user_date()  #call the var outside the defined area above
    attendees = input("Enter event attendees (comma-separated): ").split(',') # after each name the user needs to put a comma 

    # makes more events according to how many times the users makes an event
    events.append({"Title": title, "date": date, "attendees": attendees})
    print("you have added an event to your list")



def view_events():
    if not events:
        print("No upcoming events.")
        return
    print("Upcoming events:")
    for index, event in enumerate(events, start=1):
        print(f"{index}.) {event['Title']} - {event['date']}")




def view_event_details():
    view_events()
    event_index = input("Select an event to view details (enter the event number): ")
    try:
        event_index = int(event_index)
        if 1 <= event_index <= len(events):
            event = events[event_index - 1]
            print("========================================")
            print("Event Details:")
            print(f"Title: {event['Title']}")
            print(f"Date: {event['date']}")
            print("Attendees:")
            for attendee in event['attendees']:
                print(f"- {attendee}")
            print("========================================")
        else:
            print("Invalid event number. Please enter a valid event number.")
    except ValueError:
        print("Invalid input. Please enter a valid event number.")






def event_planner():
    welcome_message()
    while True:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("please select an option")
        print("1) Add an event")
        print("2) View an upcoming event")
        option = input("Please choose an option =") #prompts user to choose 1 or 2


        if option == '1': # check for user input "1" and execute code 
            add_event()
        elif option == '2':     # check for user input "2" and execute code
            view_events()
        else:
            print("------------------------------------------------")
            print("Unknown option please select between 1 and 2")
            print("------------------------------------------------")


event_planner() # execute main code block







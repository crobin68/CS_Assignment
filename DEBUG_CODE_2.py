import time

events = []
# welcome message 
def welcome_message():
    print("Welcome to your event planner")






# this is to add the event from the users input
def add_event():
    def user_date():
        while True:
            year = input("Please enter a Year : ")
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

        while True:
            day = input("Please enter a Day number: ")
            if day.isdigit() and 1 <= int(day) <= 31:
                break
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[1;31m Please enter a valid day number between 1 and 31. \033[0m")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        return f"{year}-{month}-{day}" # making sure you have all the dates in one format

    title = input("Enter an Event Title = ")
    date = user_date()
    #=======================================================================================================================================
    
    
    
    attendees = []  # make an empty list so the people can be imported into it

    done_entered = False # set (done_entered) to a false state
    while not done_entered:
        attendee = input("Enter the name of the new attendee (or type 'Done' when finished): ")
        if attendee.lower() == "done":
            done_entered = True
        else:
            attendees.append(attendee)  # Append attendee to the list


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
            print(f"Title: {event['Title']}")   #print user generated title
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









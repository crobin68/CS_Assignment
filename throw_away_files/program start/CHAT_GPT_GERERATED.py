import time

events = []

def welcome():
    print("Welcome to the event planner")




def add_event():
    print("Add an event") 
    title = input("Enter event title: ") # get input from user 
    date = input("Enter event date: ")
    attendees = input("Enter event attendees (comma-separated): ").split(',')
    events.append({"Title": title, "Date": date, "Attendees": attendees})
    print("Event added successfully!")


 

def view_events():
    if not events:
        print("No upcoming events.")
        return
    print("Upcoming events:")
    for index, event in enumerate(events, start=1):
        print(f"{index}.) {event['Title']} - {event['Date']}")





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
            print(f"Date: {event['Date']}")
            print("Attendees:")
            for attendee in event['Attendees']:
                print(f"- {attendee}")
            print("========================================")
        else:
            print("Invalid event number. Please enter a valid event number.")
    except ValueError:
        print("Invalid input. Please enter a valid event number.")




def event_planner():
    welcome()
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Here are your options")
        print("1.) Add an event")
        print("2.) View upcoming events")
        option = input("Please choose an option: ")

        if option == '1':
            add_event()
        elif option == '2':
            view_event_details()
        else:
            print("Unknown option selected, please select another option.")

        time.sleep(2)




event_planner()

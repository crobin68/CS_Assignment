import time
import sys

# all files and changes were recorded in my github, if you would like to see that please let me know


def ALL_CODE():
    #set a empty list to (events)
    events = []


    # welcome message 
    def welcome_message():
        print("Welcome to your event planner")
        time.sleep(2)

    # this is to add the event from the users input
    def add_event():
        def user_date():        # I COULD OF USED THE timedate import but some how i did not know what it was until all my code was done
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

        title = input("Enter an Event Title = ")    # get users input for the event title
        
        date = user_date()      # get (date) from (user_date())
        #=======================================================================================================================================
        
        
        
        attendees = []  # make an empty list so the people can be imported into it

        done_entered = False # set (done_entered) to a false state
        while not done_entered:
            attendee = input("Enter the name of the new attendee (or type 'Done' when finished): ")
            if attendee.lower() == "done":  # check to see if input is lowcased (done)
                done_entered = True         # stop the loop when (done_entered) is True
                break                       # break the loop 
            if attendee == "":      # check if the user entered a blank name for the attendee
                print("Please enter a valid name, you left the last one blank (no worries I did not add it to the list)")
            else:
                attendees.append(attendee)  # Append attendees to the list



        #when the user creates an event it uses this empty libery and puts all user defined vars into it
        events.append({"Title": title, "Date": date, "Attendees": attendees}) 
        
        print("You have added an event to your list") # just confirming to the user that the event was added





    # if there are no events this message displays 
    def view_events():
        if not events:
            print("No upcoming events.") # if there are no events in the list display this message
            return
        print("Upcoming events:") 
        for index, event in enumerate(events, start=1):     # if there are events that were created show the list of them
            print(f"{index}.) {event['Title']} - {event['Date']}")


    def view_event_details():
        view_events()   # call the code block (view_events)
        event_index = input("Select an event to view details (enter the event number): ") # select an event that you want to view
        try:
            event_index = int(event_index)
            if 1 <= event_index <= len(events):
                event = events[event_index - 1]
                #prints all the event details 
                print("========================================")
                print("Event Details:")
                print(f"Title: {event['Title']}")   
                print(f"Date: {event['Date']}")
                print("\x1b[4m:Attendees:\033[0m")                 
                for attendee in event['Attendees']:
                    print(f"- {attendee}")  # print all the people in a list (formated up to down)
                print("========================================")
            else:
                print("Invalid event number. Please enter a valid event number.") # if the user inputs a number that is not there send user to menu
        except ValueError:
            print("Invalid input. Please enter a valid event number.")


    def event_planner():
        welcome_message() # send the welcome message 
        while True:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("\033[0m Please select an option \033[0m")
            print("\033[1m 1) Add an event \033[0m")
            print("\033[1m 2) View upcoming events \033[0m")
            option = input("\033[3m Please choose an option: \033[0m")

            if option == '1': # if user input is ('1') then execute the block (add_event)
                add_event()
            elif option == '2': # if user input is ('1') then execute the block (view_event_details)
                view_event_details()
            elif option == '3': # if the user wants to exit the code they select option #3
                sys.exit()
            else:       # if anything else if typed this will prompt.
                print("--------------------------------------------------")
                print("\033[1m \033[1;31m Unknown option. Please select between 1 and 2 \033[0m")
                print("--------------------------------------------------")


    event_planner() # execute the whole code (lines 1-123) on screen


ALL_CODE()


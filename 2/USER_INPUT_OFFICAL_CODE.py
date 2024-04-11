import time


# event name by user input
#===============================================================

name_of_event = input("Please enter the name of the event = ")

#===============================================================




# Date of the event by the user input
#==============================================================

print("Please enter a Date of the event")
print("=======================================")
date_year = input("please enter the year = ")

if int(date_year) < 2023:
    while int(date_year) < 2023:
        print("please enter a year that is greater then 2024")
        date_year = input("please enter the year = ")

#===============================================================





# Month of the event by the user input
## if the month is not between 1-12 tell user to correct it
#===============================================================

while True:
    date_month = input("Enter the month number: ")
    if date_month.isdigit():  # Check if input is a number
        date_month = int(date_month)
        if 1 <= date_month <= 12:  # Check for input 1-12
            break  # end the while true
    print("============================================")
    print("**** Please enter a month between 1-12 ****") 


#===============================================================


# date of event by user input
#===============================================================
while True:
    date_day = input("Please enter the day = ")
    if date_day.isdigit():         #check if input is a number
        date_day = int(date_day)
        if 1 <= date_day <= 31:  # Check for input 1-31
            break  # end the while true
        print("============================================")
        print("**** Please enter a day between 1-31 ****")

#===============================================================


#------------------------------------------List of things to call and to change by user--------------------------------------------------------------------------------------------------------------------

#                     #header            #title (header)      #title (decript)    #Date: (header)                 #Date (decpipt)               #Attendees: (header)   #the rest is list of people going
event_two_stuff = [f"Event Details:"    ,    "Title: "    ,    {name_of_event}    ,    "Date:"    ,   f"{date_year}-{date_month}-{date_day}"   ,    "Attendees:"    , "Alice" , "Bob" , "Charlie"]
#------------------------------------------List of things to call and to change by user--------------------------------------------------------------------------------------------------------------------





#===========================================================================================================================================================
def show_event():
    comma2 = ',' # make sure there is a comma in-between each name 
    people2 = comma2.join(event_two_stuff[6:]) #get names of people

    print("========================================")

    print(event_two_stuff[0])                               # "event details"

    print("")                                               # blank text (spacer)

    print(event_two_stuff[1] + ", ".join(event_two_stuff[2]))          # title , name_of_event

    print(event_two_stuff[3], event_two_stuff[4])           # "Date:" , "2024-05-15"

    print(event_two_stuff[5], people2)                      # "Attendees:" and "Alice, Bob, Charlie" 

    print("========================================")
#===========================================================================================================================================================


# Get the user input for the peoples names
#==========================================================================================================================================================

def add_people():
    done_entered = False # makes done_entered to a status of False

    while not done_entered:
        new_attendee = input("Enter the name of the new attendee (or type ""Done"" when finished): ")
        if new_attendee == "Done" or new_attendee == "done": #if the user inputs "done" then set done_entered to true making the loop stop
            done_entered = True 
            show_event() #display all the details of the event 
            
            
        # Append the user input to the list
        event_two_stuff.append(new_attendee)
#===========================================================================================================================================================
add_people()




# call all the details and display the event and all its details
#===============================================================
#                                                              |
#                                                              |
#                                                              |
#===============================================================







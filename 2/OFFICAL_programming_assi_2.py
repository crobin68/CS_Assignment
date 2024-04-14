import time
import sys


# welcoming message
print("welcome to the event planner") 




def selection():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Here are your options")
    print("1.) Add an event")
    print("2.) View upcoming events")
    main_menu_option = input("Please choose an option= ")



# main menu option #1 (Add event)
    if int(main_menu_option) == 1:
        print("Add an event")


# main menu option #2 (View upcoming events)
    elif int(main_menu_option) == 2:
        print("======================================================================\n"
        "You selected option 2, please wait for the options to load...\n"
        "======================================================================")

        time.sleep(2)

        

        # choosing what event to see more detail
        def choosing_option_for_upcomming_events():
            # header for options (upcoming events)
            print("Upcoming events")

            # option 1
            print("1.) Python Workshop - 2024-05-15")

            #option #2
            print("2.) Annual Gala - 2024-06-01")

            #blank text
            print("3.) ***Please add an event***")



            pick_event = input("Please pick an event to see more detail = ")

            # make sure user chooses options 1-3
            if int(pick_event) < 0 or int(pick_event) > 4:
                print("\033[1m****INVALID OPTION****\033[0m")
                print("PLease choose an option 1-3")
                choosing_option_for_upcomming_events()

#options for (view events)
#======================================================================================================================================================================================================================================
         # view event details option #1
            if int(pick_event) == 1:


                #DETAILS FOR OPTION #1

                event_one_stuff = ["Event Details:", "Title:" , "Python Workshop" ,"Date:","2024-05-15" , "Attendees:" , "Alice", "Bob", "Charlie"]
                glue = ','
                people = glue.join(event_one_stuff[6:]) #get names of people


                print("========================================")
                print(event_one_stuff[0])                               # "event details"
                print("")                                               #  blank text (spacer)
                print(event_one_stuff[1] , event_one_stuff[2] )         # "title" , "python workshop"
                print(event_one_stuff[3], event_one_stuff[4])           # "Date:" , "2024-05-15"
                print(event_one_stuff[5], people)                       # "Attendees:" and "Alice, Bob, Charlie" 
                print("========================================")

                # prompt user if they want to go to main menu
                def go_to_main_menu():
                    startover = input("Would you like to go to the beggining?\n 1) Yes\n 2) No\n please type in the option you want = ")
                    
                    # when in event detil #1 give user option to go to main menu or term the code
                    if int(startover) == 1:
                        selection()
                        # end the program if you selects (2)
                    elif int(startover) == 2:
                        print("program ending in")
                        time.sleep(1)
                        print("3...")
                        time.sleep(1)
                        print("2...")
                        time.sleep(1)
                        print("1...")
                        time.sleep(1)
                        print("\033[31m Terminating program \033[0m")
                        sys.exit()

                go_to_main_menu() # prompt user to either end the coed or go to main menu
         
         # view event details option #2
            elif int(pick_event) == 2:
                print("43524245234234345435345345323345")
            

                print("option 2")
            
         # view event details option #3 (user makes the details)
            elif int(pick_event) == 3:
                print("option 3")

#======================================================================================================================================================================================================================================




            else: # if you put option thet is bigger then 1-3 do this
                print("")
                print("")
                print("****************************************************")
                print("invald option please select an event that exists")
                print("****************************************************")

                time.sleep(2)
                print("")
                print("")
                
                choosing_option_for_upcomming_events() # make user go back to


        choosing_option_for_upcomming_events() #calling the whole block of code
        
        
        
  #==============================================================================
 #          if user selects 3 in main menu tell them tou select between 1-2

    elif int(main_menu_option) >= 3 or int(main_menu_option) <= 0:
        print("********************************************************")
        print("| Unknown option selected, please select another option |")
        print("********************************************************")

        selection()

  #==============================================================================


# call selection (with out this nothing would happen)
selection()











attendees_input = input("Enter event attendees (comma- or space-separated): ")
attendees_list = []

# Check if the input contains commas or spaces
if ',' in attendees_input:
    # If commas are present, split by commas
    attendees_list = attendees_input.split(',')
elif ' ' in attendees_input:
    # If spaces are present, split by spaces
    attendees_list = attendees_input.split()
else:
    # If neither commas nor spaces are present, assume a single name
    attendees_list = [attendees_input]

# Now attendees_list contains a list of names
# You can access each name by its index in the list
# For example, to access the first name:
first_attendee = attendees_list[0]

# To print the list of attendees:
print("Attendees:")
for attendee in attendees_list:
    print(attendee)













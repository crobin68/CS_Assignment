import time


# prompting the user for their name and making it a variable to call
name = input("What is your name = ")

# making age = the users input
age = int(input("How old are you = "))

#getting the current year from the user
current_year = int(input("Please enter the current year = ")) 


#   Making both ints so they can subtract each other
year_birth = current_year - age 

#   Doing the math to calculate the year they will be 100
hundred_age = year_birth + 100

# calculating the years left until thye turn 100
years_until_100 = hundred_age - current_year

# checks what age you put in and sets gen_check to the option
if 0 <= age <= 11:
    gen_check = ("(Gen Z)")
if 12 <= age <= 27:
    gen_check = ("(Gen Z)")
elif 28 <= age <= 43:
    gen_check = ("(Millennial)")
elif 44 <= age <= 59:
    gen_check = ("(Gen X)")
elif 60 <= age <= 69:
    gen_check = ("(Boomer II (Generation Jones))")
elif 70 <= age <= 78:
    gen_check = ("(Boomer I)")
elif 79 <= age <= 96:
    gen_check = ("(Post War)")
elif 97 <= age <= 100:
    gen_check = ("(WWII)")



#                     FINAL PRODUCT
#      print name, age, born_year, how old you will be in 100 years
print("=====================================================================================") 
#prints the name the user inputed with a greating  
print(f"Hello {name}, Nice to meet you.")
time.sleep(1)


#prints the number(age) the user inputed                                                       
print(f"Your current age is: {age}")  

#Prints the year the user was born                            #What generation you are                                                     
print(f"The year you were born was: {year_birth} (You are apart of the {gen_check} Generation)")

#Prints the year the user will be a age 100
print(f"You will turn 100 years old on the year {hundred_age} (in {years_until_100} years)")

print("=====================================================================================")

time.sleep(15) #if running the program thru cmd prompt





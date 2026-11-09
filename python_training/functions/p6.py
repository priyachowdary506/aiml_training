#program 6: Greeting with Default Arguments
#Question: Create a function that accepts a student's name
# and a greeting message. If no greeting message is provided,
# use "Welcome" as the default.

#Solution:
def greet_msg(name,mesage= "welcome"):
    print(mesage, name)
greet_msg("rahul")
greet_msg( "Ananya","good morning")
greet_msg( "sandeep", "hello")    


# Output:
# Welcome Rahul
# Good Morning Ananya
# Hello Sandeep


# Concepts covered:
# - Default arguments
# - Function parameters
#- Function calling

# program 3: Check Even or Odd (Function with If-Else)
# Question: Write a function that accepts a number and 
# checks whether it is even or odd.

# Sample Input:
# Enter a number: 7

# Output:
# Odd Number

# Concepts covered:
# - Function parameters
# - Return statement
# - If-else conditions
# - Modulo operator

def check_even_odd(number):  
    if number % 2 == 0:       
        return "Even Number"   
    else:       
        return "Odd Number"
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(result)


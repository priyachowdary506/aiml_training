#Program 4: Find the Largest of Three Numbers
#Question: Write a function that accepts three numbers 
#and returns the largest number without 
#using the built-in max() function.

#Solution:
def find_largest(a, b, c):   
    if a >= b and a >= c:       
        return a 
    elif b >= a and b >= c:       
        return b
    return c
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = find_largest(num1, num2, num3)
print("Largest Number:", result)



# Sample Input:
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15


# Output:
# Largest Number: 25


# Concepts covered:
# - Multiple parameters
# - If-elif-else
# - Logical operators
# - Return statement

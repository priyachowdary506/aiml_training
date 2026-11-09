# Program 2: Addition of Two Numbers (Parameters and Return)
# Question: Write a function that accepts two numbers
# and returns their sum.

# Sample Input:
# Enter first number: 10
# Enter second number: 20


# Output:
# Sum: 30

# Concepts covered:
# - Parameters
# - Arguments
# - Multiple parameters
# - Return statement
# - User input
    
def add_numbers(a, b):    
    result = a + b   
    return result
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
answer = add_numbers(num1, num2)
print("Sum:", answer)

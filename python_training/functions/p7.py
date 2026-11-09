# Program 7: Factorial Using a Function and For Loop
# Question: Write a function that accepts a number and
# calculates its factorial using a for loop.

# Factorial example:
# \[
# 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
# \]

def factorial(number):    
    result = 1    
    for i in range(1, number + 1):       
        result = result * i  
    return result
num= int(input("enter a number:"))

if num < 0:   
    print("Factorial is not defined for negative numbers.")
else:    
    answer = factorial(num)   
    print("Factorial:", answer)



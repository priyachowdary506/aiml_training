# Program 10: Celsius to Fahrenheit Conversion
# Question: Write a function that converts temperature
# from Celsius to Fahrenheit.

# Formula:
# \[
# F = (C \times \frac{9}{5}) + 32
# \]

#Solution:
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32  
    return fahrenheit
temperature = float(input("Enter temperature in Celsius: "))
result = celsius_to_fahrenheit(celsius=temperature)
print("Temperature in Fahrenheit:", result)



# Sample Input:
# Enter temperature in Celsius: 37


# Output:
# Temperature in Fahrenheit: 98.6


# Concepts covered:
# - Function parameters
# - Keyword arguments
# - Return statement
# - Mathematical operations
# - User input
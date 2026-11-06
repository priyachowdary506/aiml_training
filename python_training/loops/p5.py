#question 5: Calculate Factorial of a Number
#Problem Statement:
#Write a program to accept a positive integer from the user 
#and calculate its factorial using a for loop.
#Factorial means multiplying all positive integers from 1 to the given number.
#For example:
#5! = 5 × 4 × 3 × 2 × 1 = 120
#Sample Input:
#text
#Enter a number: 5
#Expected Output:
#text
#Factorial of 5 is: 120

n= int(input("enter a positive number:"))
factorial = 1
for i in range(1,n+1):
   factorial = factorial * i
print("Factorial of", n, "is:", factorial)
 


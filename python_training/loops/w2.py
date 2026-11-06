#question 9: Sum of Digits of a Number
#Problem Statement:
#Write a Python program to accept a number from the user 
#and calculate the sum of its digits using a while loop.
#Sample Input:
#text
#Enter a number: 1234
#Expected Output:
#text
#Sum of digits: 10

n = int(input("enter a number:"))
total = 0
n = abs(n)
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print("Sum of digits:", total)

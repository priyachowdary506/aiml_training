#Question 1: Print Numbers from 1 to N
#Problem Statement:
#Write a Python program to ask the user to enter a number N.
# Use a for loop to print all numbers from 1 to N.
#Sample Input:
#text
#Enter a number: 5
#Expected Output:
#text
#1
#2
#3
#4
#5
N = int(input("enter a number N:"))
for i in range(1, N+1):
    print(i)
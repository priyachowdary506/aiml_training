#Question 2: Calculate the Sum of First N Natural Numbers
#Problem Statement:
#Write a Python program to accept a number from the user and
# calculatesum of all natural numbers from 1 to N using for loop.
#Sample Input:
#text
#Enter a number: 5
#Expected Output:
#text
#Sum of natural numbers: 15
n = int(input("enter a number :"))
total =0
for i in range(1, n+1):
  total = total +i
print(total)  

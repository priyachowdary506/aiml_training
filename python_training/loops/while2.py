#Question 8: Count the Number of Digits
#Problem Statement:
#Write a Python program to accept an integer from the user 
#and count the total number of digits using a while loop.
#Sample Input:
#text
#Enter a number: 56789
#Expected Output:
#text
#Total number of digits: 5

n= int(input("enter a number: "))
count = 0
if n == 0:
    count = 1
else:
    n = abs(n)

while n >0:
         n = n // 10
         count += 1
print("Total number of digits:", count)




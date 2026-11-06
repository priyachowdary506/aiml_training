#Question 7: Reverse a Number
#Problem Statement:
#Write a Python program to accept an integer from the user
# and reverse the number using a while loop.
#Sample Input:
#text
#Enter a number: 1234
#Expected Output:
#text
#Reversed number: 4321

n=int(input("enter a number:"))
reverse =0
while n > 0:
    digit = n % 10

    reverse = reverse * 10 + digit

    n = n // 10

print("Reversed number:", reverse)


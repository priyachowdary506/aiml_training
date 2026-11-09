# Reverse a Number (While Loop)
# Write a Python program to accept a number from the user
# and reverse it using a while loop.
# #Sample Input:
# #Enter a number: 12345
# #Expected Output:
# #Reversed number: 54321

reverse= 0
n = int(input("enter number:"))
while n> 0:
    a =n % 10
    reverse = reverse * 10 + a
    n= n//10
print("reverse number is:",reverse)    
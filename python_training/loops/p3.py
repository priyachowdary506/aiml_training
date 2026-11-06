#Question 3: Multiplication Table
#Problem Statement:
#Write a Python program to accept a number from the user
# and print its multiplication table up to 10 using a for loop.
#Sample Input:
#text
#Enter a number: 5
#Expected Output:
#text
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50

n= int(input("enter a number:"))
for i in range(1,11):
  print(n, "x", i, "=", n * i)
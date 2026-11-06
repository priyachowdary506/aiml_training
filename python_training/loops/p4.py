#Question 4: Count Even and Odd Numbers
#Problem Statement:
#Write a Python program to accept a number N 
#and count how many even and odd numbers exist between 1 and N
# using a for loop.
#Sample Input:
#text
#Enter a number: 10
#Expected Output:
#text
#Even numbers count: 5
#Odd numbers count: 5

n = int(input("enter a number:"))
even =0
odd =0
for i in range(1,n+1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers count:", even)
print("Odd numbers count:", odd)


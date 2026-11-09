#Find the Largest Number (For Loop)
#Write a Python program to accept 5 numbers from the user
# and find the largest number using a for loop.
#Sample Input:
#Enter number 1: 25
#Enter number 2: 45
#Enter number 3: 12
#Enter number 4: 89
#Enter number 5: 34
#Expected Output:
#Largest number: 89
largest =0
for i in range(1,6):
    n= int(input(f"enter  numbers{i}:"))
    if n> largest:
       largest = n
print("largest number:", largest)          
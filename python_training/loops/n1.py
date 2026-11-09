# Print a Star Pattern (Nested For Loop)
# Problem Statement:

# Write a Python program to accept the number of rows from the user
# and print the following star pattern using a nested for loop.
# Sample Input:
# Enter number of rows: 5
# Expected Output:
# *
# **
# ***
# ****
# *****
rows= int(input("enter number of rows:"))
for i in range(1,rows + 1):
    for j in range(1 , i + 1):
        print("*", end ="")
    print()    

        
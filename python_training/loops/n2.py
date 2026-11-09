# Print a Number Pattern (Nested While Loop)
# Problem: Accept the number of rows from the user
# and print the following pattern using nested while loops.
# Sample Input:
# Enter number of rows: 5
# Expected Output:
# 1
# 12
# 123
# 1234
# 12345
rows =int(input("enter number of rows:"))
i=1 
while i<= rows:
    j=1
    while j<=i:
        print(j, end ="")
        j +=1
    print()  
    i+=1  
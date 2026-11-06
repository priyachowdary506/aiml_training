#question 5: Pass or Fail
#Write a program to:
#- Accept student marks.
#- If marks are 35 or above, print "Pass".
#- Otherwise, print "Fail".
marks= float(input("enter student marks:"))
if marks>=35:
    print("pass")
else:
    print("Fail")

 #Write a program to:
#- Accept two numbers.
#- Print the greater number.
#- If both numbers are equal, print "Both numbers are equal".
#Part 3: If...Elif...Else Statements
#Objective: Check multiple conditions.
num1= float(input(" enter first number:"))
num2 = float(input("enter second number:"))

if num1 > num2:
    print("greatest number is:", num1)
elif num2 > num1:
    print("greatest number is:", num2)
else:
    print("both numbers are equal")        

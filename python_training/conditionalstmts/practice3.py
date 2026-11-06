#Question 7: Grade Calculator
#Write a program to accept student marks and display the grade.
#Marks	Grade
#90–100	A
#75–89	B
#60–74	C
#35–59	D
#Below 35	Fail
#Also handle marks outside the 0–100 range.
marks = float(input("enter student marks:"))
if marks <0 or marks >100:
    print("Invalid input") 
elif marks>= 90 and marks<= 100:
    print("A grade")
elif marks >= 75 and marks <=89:
    print("B grade")  
elif marks>=60 and marks<=74:
    print("C grade")
elif marks>=35 and marks<=59:
    print(" D grade")
else:
    print("Fail")           

#Question 8: Number Classification
#Write a program to check whether a number is:
#- Positive
#- Negative
#- Zero
num = int(input("enter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")    
else:
    print(("zero"))    

#question 9: Simple Calculator
#Ask the user to enter two numbers and an operator (+, -, *, /).
#Use if...elif...else to perform the selected calculation.
# Display an error for an unsupported operator and
# prevent division by zero.
n1= float(input("enter first number:"))
n2= float(input("enter second number:"))
operator = input("enter operator(+, -, *, /):")
if operator =="+":
    print(n1+n2)
elif operator == "-":
    print(n1-n2)   
elif operator == "*":
    print(n1*n2)        
elif operator == "/":
    if n2 ==0:
        print("cannot divide by zero")
    else:    
        print(n1/n2)  
else:
    print("unsupported operator")     

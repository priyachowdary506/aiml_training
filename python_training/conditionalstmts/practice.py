#Write a Python program to check whether a student is eligible
# to write an examination.

#Conditions:
#1. Ask the student to enter their age.
#2. If the age is 18 or above, ask whether the student has paid
# the exam fee.
#3. If the exam fee is paid, display "You are eligible to
# write the exam."
#4. Otherwise, display "Please pay the exam fee."
#5. If the age is below 18, display "You are not eligible."

age = int(input("enter age:"))
if age>=18:
  feepaid = input("have you paid exam fee yes/no:")
  if feepaid == "yes":
    print("you are eligible to write exam")
  else:
    print("please pay the exam fee")
else:
    print("you are not eligible")            
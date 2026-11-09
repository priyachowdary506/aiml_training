# #program 5: Student Details (Positional and Keyword Arguments)
# #Question: Create a function that accepts a
# # student's name, age, and course.
# # Call the function using both positional and 
# #keyword arguments.
# Output:
# Name: Rahul
# Age: 22
# Course: Python
# ----------------
# Name: Ananya
# Age: 21
# Course: AI/ML

# Concepts covered:
# - Multiple parameters
# - Positional arguments
# - Keyword arguments
def student_details(name,age, course):
    print("name:", name)
    print("age:", age)
    print("course:", course)
student_details("Rahul", 22, "Python")
print("-------------") 
student_details("Ananya", 21, "AI/ML")


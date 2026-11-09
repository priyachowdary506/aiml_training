#Program 8: Calculate Average Marks (List and Built-in Functions)
#Question: Write a function that accepts a list of student
# marks and calculates the average using sum() and len().

#Solution:
def calculate_average(marks):
    if len(marks) == 0: 
        return None
    total = sum(marks)  
    average = total / len(marks)   
    return average
student_marks = [80, 90, 70, 100]
result = calculate_average(student_marks)
if result is None:   
    print("No marks available")
else:    
    print("Average Marks:", result)



# Output:
# Average Marks: 85.0


# Concepts covered:
# - Functions
# - Lists
# - Built-in functions
# - sum()
# - len()
# - Return statement

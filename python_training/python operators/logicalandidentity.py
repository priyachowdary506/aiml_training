age = 22
has_id = True
print(age >= 18 and has_id) # True
print(age < 18 or has_id) # True
print(not has_id) # False

#identity operator
first = [1, 2, 3]
second = [1, 2, 3]
third = first
print(first == second) # True: values are equal
print(first is second) # False: separate list objects
print(first is third) # True: same object
print(first is not second) # True



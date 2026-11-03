#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the item with the specified value
#del()  removes specific index

numbers = [10, 20, 20]

numbers.append(30)   
print(numbers)    # [10, 20, 20, 30]

numbers.extend([40, 50])
print(numbers)   # [10, 20, 20, 30, 40, 50]

numbers.insert(1, 15)  
print(numbers)    # [10, 15, 20, 20, 30, 40, 50]

print(numbers.count(20)) # 2
print(numbers.index(30)) # 4

numbers.remove(20)     
print(numbers)  # Removes the first 20

last = numbers.pop()   
print(numbers)   # Removes and returns 50

copied = numbers.copy()
print(numbers)    # Creates a shallow copy

numbers.clear()
print(numbers)  
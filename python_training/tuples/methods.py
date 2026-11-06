#count() - returns number of items appear in the tuple
#syntax   tuple.count(value)
t= (10,20,30,10,"hi",2.5,"hi",20)
print(t.count(10))
print(t.count("hi"))
print(t.count(2.5))

#index() - returns index of the first occurance in the tuple 
#syntax - tuple.index(value)
print(t.index(10))
print(t.index(20))
print(t.index("hi"))

#len() - retuns total no of elements in tuple
#syntax - len(tuple)
print(len(t))

#sorted() - returns sorted list from the tuple 
#syntax - sorted(tuple)
t1= (25,15,5,10,30)
print(sorted(t1))

# tuple() - converts iterable(like list) into na tuple
#syntax - tuple(iterable)
t2= [10,20,"hi",2.5]
print(tuple(t2))
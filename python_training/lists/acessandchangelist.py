# first iem start from 0 
#Negative indexing means start from the end
#-1 refers to the last item, 
#-2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])  # cherry because last item index from -1

#range of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # prints only 2,3,4 dont print 5 - c,o,k

# 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # retuns from 0 to 3 

# 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #reurns from 2 to end 

#returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # retuns orange to melon 

#item present in the list we use - in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#CHANGE
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #  replace banana with blackcurrant 

#range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#change 2 and replacing with 2 new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#replacing with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#use insert()
a=[10,20,25]
a.insert(2,55)
print(a)
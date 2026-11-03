#List -  ordered and changeable. Allows duplicate members.
#Tuple- ordered and unchangeable. Allows duplicate members.
#Set  - unordered, unchangeable*,unindexed. No duplicate members.
#Dictionary- ordered** and changeable. No duplicate members.

# list 
#Ordered
#lists are ordered - items have a defined order, and order will not change.
#add new items to a list,new items placed at the end of the list.

#Changeable
#list is changeable-we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
#lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#allow duplicate values
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# to findout length we use len()
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#list can be any data type like string,int,boolean
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#list  with different datatypes
list1 = ["abc", 34, True, 40, "male"]
print(type(list1[0]))

# datatype of list type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
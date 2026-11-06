#accessing elements 
#positive index starts from 0 from left to right
#negetive index starts from -1 from right to left 
t =(10,20,"hi",2.5,30,5.5)
print(t[0])
print(t[5])
print(len(t))   # to check length of t 
print(type(t[2]))  # to check datatype

#slicing  
print(t[1:4])
print(t[-1:])
print(t[:5])

#concatination
t1= (1,2,3,4)
t2=("hi","hello", 2.5)
t3= t1+t2
print(t3)

#repetition
b=(5,6)
c= b*3
print(c)

#checking elements - we use in 
a1=(10,2.4,"hi",45)
print(10 in a1)
print("hi" in a1)
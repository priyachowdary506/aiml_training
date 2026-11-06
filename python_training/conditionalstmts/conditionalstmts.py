age =int(input("enter your age:"))
if age>=18:
    print("is eligible to vote")
else: 
    print("not eligible to vote")

#multiple if statements - we use elseif 
marks =float(input("enter your marks:"))
if marks>=75:
    print("distinction")
elif marks >=60:
    print("pass")
elif marks>=55: 
    print("firstclass")          
else: 
    print("fail")


#short if- in single line we will execute
if age >=18: print("eligible")
result = "adult" if age>=18 else "minor" 
print(result)
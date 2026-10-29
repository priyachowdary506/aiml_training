#in python we cannt combine strings and numbers, in order to use that we need top use f-string or fomat() method
age = 20
text =f"my name is john, i am {age}"
print(text)
#placeholders and modifiers
#add price holder for the price variable
price = 30
text1= f"the price is {price} dollars"
print(text1)

#display price with 2decimals need to use .2f
price = 35
text2= f"the price is {price:.2f} dollars"
print(text2)
#math operation
price = 300
text3= f"the price is {price*40} dollars"
print(text3)
def calculate_average(mark1, mark2, mark3):
 average = (mark1 + mark2 + mark3) / 3
 return average
m1 = float(input("Enter first mark: "))
m2 = float(input("Enter second mark: "))
m3 = float(input("Enter third mark: "))
avg = calculate_average(m1, m2, m3)
print("Average marks:", avg)
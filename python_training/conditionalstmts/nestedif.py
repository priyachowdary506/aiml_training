#nestedif - a nestedif is an if stmt placed inside another 
#if r else block
username = "student1"
password = "python123"
if username == "student":
 if password == "python123":
   print("Login successful")
 else:
   print("Incorrect password")
else:
   print("Username not found")
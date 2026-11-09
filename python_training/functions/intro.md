1. What Is a Function?
A function is a reusable block of code that performs a particular task. Instead of writing the same instructions
again and again, we can place them inside a function and call the function whenever we need it.
Example from daily life: A coffee machine performs a set of steps whenever you press its button. Similarly, a
Python function runs a set of instructions when it is called.
def greet():
print("Hello, welcome to Python!")
greet()

Output
Hello, welcome to Python!
In this example, def defines the function, greet is its name, and greet() calls (executes) it.
2. Why Do We Use Functions?
• Code reusability: Write code once and use it many times.
• Less repetition: Avoid copying the same code into multiple places.
• Easy maintenance: Update the logic in one place.
• Better organization: Divide a large program into smaller tasks.
• Testing and debugging: Smaller functions are easier to check.
3. Syntax of a Function
def function_name():
# statements
    statement_1
    statement_2
function_name()
Important points:
• Use the def keyword to define a function.
• Choose a meaningful function name. Use lowercase words separated by underscores, such as
calculate_total.
• Parentheses () are required after the function name.
• The function body must be indented.
• A function runs only when it is called.
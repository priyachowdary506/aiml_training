#PASS 
#if statements cannot be empty,
# but if you for some reason 
#have an if statement with no content,
# put in the pass statement to avoid getting an error.
#MATCH
#Instead of writing many if..else statements,
# you can use the match statement.
#match statement selects one of many code blocks to be executed.

print("Welcome to AI Assistant!")
print("1. Greeting")
print("2. Weather")
print("3. Learning Python")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("AI Bot: Hello! How can I help you?")

    case 2:
        print("AI Bot: I can help you check weather information.")

    case 3:
        print("AI Bot: Let's start learning Python!")

    case 4:
        print("AI Bot: Goodbye! Have a nice day.")

    case _:
        print("AI Bot: Invalid choice. Please try again.")
# Example: Using the built-in debugger with breakpoint()

def greet(name):
    message = f"Hello, {name}!"
    breakpoint()  # Pauses execution here
    print(message)
    return message

# Call the function
greet("Alice")


# l - List surrounding lines of code (see where you are)
# p name - Print the value of the variable name
# p message - See what’s inside message
# n - Go to next line (print(message))
# c - Continue execution (exit debugger and run remaining code)
# q - Quit debugger immediately

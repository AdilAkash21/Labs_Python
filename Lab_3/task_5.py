
# Fix using a docstring 

def greet(Adil):
    """Greets a person by name."""
    
    print(greet("Adil"))
    
# Fix using pass

def greet(name):
    # finish later
    pass

print(greet("Adil"))

# Complete Program 

def greet(name):
    """Greets a person by name."""
    return "Greeting, " + name + "!"

name = input("Enter your name: ")
print(greet(name))
# 1. Syntax Error — Missing colon after def

def greet()   # missing colon
    print("Hello")


# 2. Conceptual Error — Wrong slice boundaries (runs, but wrong result)

s = "Adil Akash"
print(s[:2])   # expected "Adil", but gives "Ad"


# 3. Syntax Error — Missing closing parenthesis

print("Hello"   # missing )
      
    
# 4. Conceptual Error — Wrong variable used
a = 10
b = 5

result = a + a   # should be a + b
print(result)


# 5. Syntax Error — Bad indentation

def say_hi():
print("Hi")   # not indented

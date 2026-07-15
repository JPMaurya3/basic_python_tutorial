def add(a, b):  
    return a + b

result = add(10, 20)
print(result)

#optional parameter
def greet(name="Guest"):
    print(name)

greet()
greet(input("Enter your name: "))
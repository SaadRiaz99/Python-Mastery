"""Day 9: Understand __name__. Importing this module must not run the demo."""

def greet(name):
    return f"Hello, {name}!"

def demo():
    print(greet("Saad"))

if __name__ == "day_09_imports":
    demo()

assert greet("Saad") == "Hello, Saad!"
print("Day 9 passed")

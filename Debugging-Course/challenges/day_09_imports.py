"""Day 9: Understand __name__. Importing this module must not run the demo."""

def greet(name):
    return f"Hello, {name}!"

def demo():
    print(greet("Sumaiya Rani"))

if __name__ == "__main__":
    demo()

assert greet("Sumaiya Rani") == "Hello, Sumaiya Rani!"
print("Day 9 passed")

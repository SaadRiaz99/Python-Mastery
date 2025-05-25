# Python Conditionals

# Basic if statement
age = 18
if age >= 18:
    print('You are an adult')

# If-else
score = 75
if score >= 60:
    print('Passed!')
else:
    print('Failed!')

# If-elif-else
grade = 85
if grade >= 90:
    print('Grade: A')
elif grade >= 80:
    print('Grade: B')
elif grade >= 70:
    print('Grade: C')
elif grade >= 60:
    print('Grade: D')
else:
    print('Grade: F')

# Nested conditionals
num = 15
if num > 0:
    if num % 2 == 0:
        print('Positive Even')
    else:
        print('Positive Odd')
elif num < 0:
    print('Negative')
else:
    print('Zero')

# Ternary operator
x = 10
result = 'Even' if x % 2 == 0 else 'Odd'
print(f'{x} is {result}')

# Logical operators
age = 25
has_id = True
if age >= 18 and has_id:
    print('Entry allowed')

if age < 18 or not has_id:
    print('Entry denied')

# Match statement (Python 3.10+)
command = 'start'
match command:
    case 'start':
        print('Starting...')
    case 'stop':
        print('Stopping...')
    case 'pause':
        print('Pausing...')
    case _:
        print('Unknown command')


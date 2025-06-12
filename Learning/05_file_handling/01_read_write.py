# Python File Handling

# Writing to file
with open('example.txt', 'w') as f:
    f.write('Hello, World!\\n')
    f.write('This is a test file.\\n')
    f.write('Python file handling is easy!\\n')

print('File written successfully!')

# Reading entire file
with open('example.txt', 'r') as f:
    content = f.read()
    print('Entire file:')
    print(content)

# Reading line by line
with open('example.txt', 'r') as f:
    print('Line by line:')
    for line in f:
        print(line.strip())

# Reading into list
with open('example.txt', 'r') as f:
    lines = f.readlines()
    print(f'Lines as list: {lines}')

# Appending to file
with open('example.txt', 'a') as f:
    f.write('This line was appended!\\n')

# Working with CSV
import csv

# Writing CSV
data = [
    ['Name', 'Age', 'City'],
    ['Saad', 25, 'Karachi'],
    ['Ali', 23, 'Lahore'],
    ['Ahmed', 27, 'Islamabad'],
]

with open('people.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print('CSV written!')

# Reading CSV
with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Working with JSON
import json

# Writing JSON
data = {
    'name': 'Saad',
    'age': 25,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'address': {
        'city': 'Karachi',
        'country': 'Pakistan'
    }
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

print('JSON written!')

# Reading JSON
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(f'Loaded: {loaded}')


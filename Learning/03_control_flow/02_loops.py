# Python Loops

# For loop
print('Counting:')
for i in range(1, 6):
    print(i, end=' ')
print()

# For loop with list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f'I like {fruit}')

# For loop with enumerate
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')

# While loop
print('\\nWhile loop:')
count = 0
while count < 5:
    print(count, end=' ')
    count += 1
print()

# Break and continue
print('\\nBreak example:')
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print()

print('Continue example:')
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()

# Nested loops
print('\\nMultiplication table:')
for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i}*{j}={i*j}', end='  ')
    print()

# Loop with else
print('\\nFor-else:')
for i in range(5):
    if i == 10:
        break
else:
    print('Loop completed without break')

# Zip function
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f'{name}: {score}')


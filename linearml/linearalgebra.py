x : float = int(input("Enter a number: "))


left = 3 * (x -2)/4 +  (x + 5) / 2
right = 2 * x- 1

print("Left side:", left)
print("Right side:", right)


difference = abs(left - right)
print("Difference:", difference > 0.0001)

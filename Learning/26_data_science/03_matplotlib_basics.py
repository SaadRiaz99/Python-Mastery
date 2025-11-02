# Matplotlib Basics

import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label='Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Plot')
plt.legend()
plt.savefig('line_plot.png')
plt.close()

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 20]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.savefig('bar_chart.png')
plt.close()

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.savefig('scatter_plot.png')
plt.close()

print('Plots saved!')


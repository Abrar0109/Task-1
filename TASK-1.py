import matplotlib.pyplot as plt

# Data
ages = [22, 25, 29, 31, 35, 38, 40, 42, 45, 50, 52, 55, 58, 60, 62, 65, 70, 72, 75, 80]

# Create histogram
plt.hist(ages, bins=8, edgecolor='black')

# Add titles and labels
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Individuals')

# Show the plot
plt.show()


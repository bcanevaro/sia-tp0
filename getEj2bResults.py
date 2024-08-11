import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import json

with open(f"{sys.argv[1]}", "r") as f:
        config = json.load(f)
        ball = config["pokeball"]
        pokemon = config["pokemon"]

cvs_file= "ej2b.csv"
data=pd.read_csv(cvs_file)

# Calculate mean and standard deviation for each point
mean_y = data.mean(axis=0)
std_dev_y = data.std(axis=0)

# Calculate upper and lower bounds
upper_bound = mean_y + std_dev_y
lower_bound = mean_y - std_dev_y

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(0, 100, 1)

# Plot the mean value
ax.plot(x, mean_y, label='Mean Value', color='blue')

# Plot the shaded area representing the range ±1 standard deviation
ax.fill_between(x, lower_bound, upper_bound, color='blue', alpha=0.2, label='±1 Std Dev')

# Customize the plot
ax.set_title('Catch rate vs HP % for Caterpie with a Pokeball')
ax.set_xlabel('HP %')
ax.set_ylabel('Catch rate')
ax.legend()

# Show the plot
plt.show()

import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# Load configuration and data
with open(f"{sys.argv[1]}", "r") as f:
    config = json.load(f)
    ball = config["pokeball"]
    pokemon = config["pokemon"]

cvs_file = "ej2b.csv"
data = pd.read_csv(cvs_file)

# Calculate mean and standard deviation for each point
mean_y = data.mean(axis=0)
std_dev_y = data.std(axis=0)

# Calculate upper and lower bounds
upper_bound = mean_y + std_dev_y
lower_bound = mean_y - std_dev_y

# Create a colormap from green to yellow to red
cmap = LinearSegmentedColormap.from_list("mycmap", ["red", "yellow", "green"])

# Generate x values
x = np.arange(len(mean_y))

# Prepare segments for LineCollection
points = np.array([x, mean_y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Normalize color values based on x-axis
norm = plt.Normalize(x.min(), x.max())
colors = cmap(norm(x))

# Create LineCollection
lc = LineCollection(segments, colors=colors, linewidth=2)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Add the LineCollection to the plot
ax.add_collection(lc)

# Plot the shaded area representing the range ±1 standard deviation
ax.fill_between(x, lower_bound, upper_bound, color='grey', alpha=0.2, label='±1 Std Dev')

# Customize the plot
ax.set_title(f'Catch rate vs HP % for {pokemon} with a {ball}')
ax.set_xlabel('HP %')
ax.set_ylabel('Catch rate')
ax.legend()

# Auto-scale both axes
ax.autoscale_view()

# Show the plot
plt.show()

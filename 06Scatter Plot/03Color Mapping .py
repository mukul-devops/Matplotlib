'''
- Color Mapping :
    Instead of giving every point the same color, color can represent another numerical feature.



- cmap parameter: cmap stands for colormap. It’s a mapping from numerical values to colors.
                   When you pass a list/array of numbers to the c parameter in plt.scatter(),
                   Matplotlib uses cmap to convert those numbers into colors.
      =>  cmap as the color palette that translates data values into a gradient.
    
    Popular Colormaps(cmap):
    "viridis"
    "plasma"
    "inferno"
    "cool"
    "hot"
    "rainbow"
    "jet"

    viridis is generally recommended because it is perceptually uniform and colorblind-friendly.


- plt.colorbar(): Adds a color scale legend to the chart.
                  It shows how the numeric values map to colors, making the visualization interpretable.
'''

import matplotlib.pyplot as plt

hours = [2,3,4,5,6]
marks = [55,60,68,75,85]
attendance = [60,70,75,90,95]

plt.scatter(
    hours,
    marks,
    c=attendance,       # assigns a numeric value to each point.
    cmap="viridis",     #  maps those values to a gradient color scale.
    s=150
)

plt.colorbar(label="Attendance")   #adds a legend showing the color scale.


# Now:    Position → Hours and Marks
#         Color → Attendance
#         Size → Fixed

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()
'''
Method 2 (Industry Standard): plt.subplots()
        This is the method you'll use in 95% of real-world projects.

Modern Approach:
    Instead of calling plt.subplot() repeatedly, you can use plt.subplots() to create a grid of axes at once.
    This is cleaner and more flexible, especially for larger grids.

    fig, ax = plt.subplots(nrows, ncols, figsize=(10,4))

    fig → The overall figure object (the canvas).
    ax(axes) → An array of subplot axes objects (individual plots).
    nrows → Number of rows in the subplot grid.
    ncols → Number of columns in the subplot grid.
    figsize → Size of the entire figure (width, height in inches).

    Now you are working directly with Figure and Axes objects.

Understanding:
    fig, ax = plt.subplots(1,2)

    Meaning:1 Row, 2 Columns
    Visualization:
    +-------------+-------------+
    |   Axes 0    |   Axes 1    |
    +-------------+-------------+

    ax[0].plot([1,2,3],[2,4,6])   # this plot fuction work on Axes 0
    This is called the Object-Oriented (OO) API, and it's the recommended style for professional code.



'''

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2,2, figsize=(10,8),dpi=100, facecolor='lightgreen')   # With figsize The entire figure becomes larger.

''' Now:
+------------+------------+
| ax[0,0]    | ax[0,1]    |
+------------+------------+
| ax[1,0]    | ax[1,1]    |
+------------+------------+
'''

# Line Plot
ax[0,0].plot([1,2,3,4],[2,5,3,7])
ax[0,0].set_title("Line Plot")

# Bar Chart
ax[0,1].bar(
    ["A","B","C"],
    [5,3,7]
)
ax[0,1].set_title("Bar Chart")

# Scatter Plot
ax[1,0].scatter(
    [1,2,3,4],
    [5,2,6,8]
)
ax[1,0].set_title("Scatter Plot")

# Histogram
data = np.random.normal(50,10,200)   #50 mean, 10 std, 200 size

ax[1,1].hist(
    data,
    bins=15
)
ax[1,1].set_title("Histogram")

plt.show()

'''
Notice Something?
Earlier, we used:  plt.title()
Now we write:      ax.set_title()

Similarly:
Old (plt)	    New (ax)

plt.title()	    ax.set_title()
plt.xlabel()	ax.set_xlabel()
plt.ylabel()	ax.set_ylabel()
plt.grid()	    ax.grid()
plt.legend()	ax.legend()

This lets you customize each subplot independently.




'''

'''
Subplots - A subplot is a way to display multiple plots in a single figure. 
           This is especially useful when you want to compare different visualizations side by side.

Method 1: plt.subplot() - 

         plt.subplot(nrows, ncols, index)

            nrows → Number of rows in the grid.
            ncols → Number of columns in the grid.
            index → Position of the plot (starts at 1).

Understanding the Position Number
    plt.subplot(1, 2, 1)
    means: 1 rows, 2 columns, 1st position

    Visualize it:
    +---------+---------+
    |  plot1  |  plot2  |
    +---------+---------+

    plt.plot([1,2,3],[2,4,6])   
    plt.title('line chart')         # these fuction work on plot1

    This is called State-based API

'''

import matplotlib.pyplot as plt

plt.figure( dpi=120, facecolor="lightyellow", edgecolor="blue", linewidth=2)

plt.subplot(2,2,1)
plt.plot([1,2,3],[2,4,6])
plt.title('line chart')

plt.subplot(2,2,2)
plt.bar(["A","B","C"],[3,5,2])
plt.title('bar chart')

plt.subplot(2,2,3)
plt.scatter([1,2,3],[5,2,8])
plt.title('scatter chart')

plt.subplot(2,2,4)
plt.pie([40,30,20,10])
plt.title('pie chart')

plt.tight_layout()   # automatically adjusts spacing.
plt.show()
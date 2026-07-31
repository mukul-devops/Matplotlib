'''
An Area Plot is simply a Line Plot with the area under the line filled with color.

plt.fill_between() - This function fills the area between two curves (or between a curve and a baseline),
                 making it perfect for visualizing ranges, cumulative values, or highlighting regions.

                plt.fill_between(x, y)
                  x - The horizontal x-coordinates that define the curves.
                  y - The y-coordinates that defining the curve

                Customization:
                plt.fill_between(x, y,
                                 color='c',
                                 alpha=0.4
                                 )

                color - color of area.
                Alpha - Transparency (0 = invisible, 1 = solid)

                 
'''

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [20,25,35,30,40]

plt.fill_between(months, sales,
                 color='c',
                 alpha=0.7,
                 )



#Add Line + Filled Area
#Professional charts usually include both.

months = ["Jan","Feb","Mar","Apr","May","Jun"]
sales = [15,20,25,30,40,45]

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(
    months,
    sales,
    color="blue",
    linewidth=2
)

ax.fill_between(
    months,
    sales,
    color="lightblue",
    alpha=0.4
)

ax.set_title("Monthly Sales")
ax.set_xlabel('Months')
ax.set_ylabel('Sales')
ax.grid(alpha=0.3)

plt.show()

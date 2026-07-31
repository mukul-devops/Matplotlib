'''
plt.stackplot() - 
        It is used to create stacked area plots, which are great for visualizing cumulative data trends over time.
        Think of it as layers of data stacked on top of each other,
        showing both individual contributions and the overall total.

        Purpose: Displays multiple datasets stacked together as filled areas.
        X-axis: Typically represents time or sequential values.
        Y-axis: Represents quantities that are stacked cumulatively.

        When to Use:
        Showing composition of totals over time (e.g., sales by product category).
        Visualizing resource usage (e.g., CPU, memory, disk).
        Tracking population growth across groups.



    plt.stackplot(x,y1,y2,y3,
                  labels,
                  colors,
                  alpha = 0.6)

        x: The sequence of values (e.g., time, categories).
        y1, y2, ...: Multiple datasets to stack.
        labels: Optional labels for each dataset.
        colors: Optional colors for each area.
        alpha → Transparency (0 = fully transparent, 1 = opaque).



'''

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]

IT = [10,12,13,15,17]
HR = [5,6,7,8,8]
Sales = [15,18,20,23,25]

fig, ax = plt.subplots(figsize=(10,6))

labels=["IT","HR","Sales"]
colors=[ "skyblue","orange", "green"] 
    
ax.stackplot( months,IT,HR,Sales,
             labels=labels,
             colors=colors,
             alpha=0.8
            )


ax.legend(loc="upper left")
ax.set_title("Department Revenue")
ax.grid(alpha=0.3)

plt.show()


'''
1. What is an Area Plot?
    A line plot where the area below the line is filled to emphasize the magnitude of values.

2. What is a Stack Plot?
    A plot that displays how multiple datasets contribute to a cumulative total over time.

==>Area Plot vs Stack Plot
        Area Plot	                Stack Plot
        One dataset	                Multiple datasets
        Uses fill_between()	        Uses stackplot()
        Shows one trend	Shows       contribution of multiple categories
        Good for revenue trend	    Good for composition over time
'''
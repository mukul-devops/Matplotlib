'''
1. Shared Axes (sharex and sharey)


    fig, ax = plt.subplots(
        2, 1,
        sharex=True,
        sharey=True
    )

    sharex - Share the X-axis among subplots(True, False, "col", "row")  	 ,   sharex=True

    sharey - Share the Y-axis among subplots	                             ,   sharey=True

    Suppose we compare monthly sales from two stores.
    Without shared axes: Both graphs have separate x-axis labels.
    Using sharex: Both Axes use the same x-axis.
    
    Using sharey: Now both plots use the same y-axis scale.
                  Very useful for comparing values fairly.

    Benefits: Cleaner dashboard
              Easier comparison
              Less repeated labeling

              
2. tight_layout(): One of the most frequently used functions.
    Title, xlabel overlaps
    Subplots may overlap.    

    plt.tight_layout() - automatically adjusts spacing.

    Use this in almost every multi-plot figure.

    
3. constrained_layout=True
    Modern alternative to tight_layout().

    fig, ax = plt.subplots( 2,2,
                            constrained_layout=True
                            ) 
    
    Advantages:
        Better spacing
        Handles colorbars more gracefully
        Works well with complex layouts
    Generally, choose either tight_layout() or constrained_layout, not both together.

    
4. Figure Title (fig.suptitle()) 
    Each subplot has its own title:
        ax[0,0].set_title("Sales")

    But sometimes you want one title for the entire figure.
        fig.suptitle(
            "Company Performance Dashboard",
            fontsize=16
        )

        
5. Understanding the axes Array 
    Suppose:
            fig, ax = plt.subplots(2,2)

            ax is a NumPy array.
            ax contains:[[ax00 ax01]
                         [ax10 ax11]]

            Access them like this:
                ax[0,0]
                ax[0,1]
                ax[1,0]
                ax[1,1]

6. Flatten the Axes:
    A very common professional technique.
    ax = ax.flatten()    #flatten the ax array.
    Now Access them like this:
        ax[0]
        ax[1]
        ax[2]
        ax[3]

    Now we can use them like this: ax[0].plot([1,2,3,4],[2,5,3,7]) ,
    Instead of: ax[0,0].plot([1,2,3,4],[2,5,3,7])
    Much easier.


7. Loop Through Subplots 

    Instead of writing:
        ax[0].grid()
        ax[1].grid()
        ax[2].grid()
        ax[3].grid()

    Use a loop -
        for axis in ax:
            axis.grid(True)

    This is cleaner and scales to many plots.   


8. Remove Unused Subplots
    Suppose you create:
    fig, ax = plt.subplots(2,2)
    You only need 3 plots.



    Delete the extra or worth subplot.
        fig.delaxes(ax[1,1])     #delete 4th plot

        #When ax is flatten use this to delete 4th plot 
        fig.delaxes(ax[3])      

9. Rotate Ticks
    Very common.

        ax.tick_params(
            axis="x",
            rotation=45
        )

    Useful when category names are long.


    
'''

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

sales_A = [20, 25, 30, 35]
sales_B = [18, 22, 28, 32]
sales_c = [15, 19, 25, 35]


fig, ax = plt.subplots(2, 2,
                       sharex=True,
                       constrained_layout=True,
                       facecolor='skyblue'
                       )
ax = ax.flatten()

fig.suptitle(
            "Company Performance Dashboard",
            fontsize=16,
            color='purple',
            weight='bold'
            )
        
ax[0].plot(months, sales_A)
ax[0].set_title("Store A")

ax[1].plot(months, sales_B)
ax[1].set_title("Store B")

ax[2].plot(months, sales_c)
ax[2].set_title("Store C")

for axis in ax:
            axis.grid(alpha=0.3)

fig.delaxes(ax[2])
fig.delaxes(ax[3])

plt.show()

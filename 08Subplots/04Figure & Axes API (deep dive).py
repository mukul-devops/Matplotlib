'''
Figure & Axes API (Deep Dive):
    This is how professional Python developers write Matplotlib code.

    If you open Kaggle notebooks, GitHub repositories, or production ML projects, you'll rarely see only:
    plt.plot(x, y)

    Instead, you'll usually see:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Sales")
    ax.set_xlabel("Month")
    ax.grid(True)

    The reason is that the Object-Oriented (OO) API gives much more control.
    If you use only plt, things become difficult to manage.
    With the Figure & Axes API, each chart is independent.


    Understanding the Hierarchy :
        Figure
        │
        ├── Axes
        │     ├── X-axis
        │     ├── Y-axis
        │     ├── Title
        │     ├── Grid
        │     ├── Legend
        │     └── Plot
        │
        ├── Axes
        │
        └── Axes   

    Remember:
    Figure → Whole canvas
    Axes → One plotting area
    Axis → X-axis or Y-axis
    Many beginners confuse Axes and Axis.


    Usually, we create both the figure and axes together:
    fig, ax = plt.subplots(2, 3,
                           figsize=(10,6), 
                           dpi=100, 
                           facecolor="lightyellow", 
                           edgecolor="blue", 
                           linewidth=2)
            2,3                 nrows=2, ncols=3(2 Row, 3 Columns) total 6 Axes
            figsize	            Set figure size in inches (width, height)	    
            dpi             	Resolution (dots per inch)	                    
            facecolor       	Background color of the figure              	
            edgecolor       	Border color of the figure                  	
            linewidth       	Thickness of border	                           
            frameon         	Show/hide frame (default True)              	

     fig.set_facecolor("lightgray")    # also set figure color like this.
    

    ax.set_xlim(2,4) and ax.set_ylim(20,80)  is used to set limit of x-axis and y-axis
    Useful for zoom in/out

    Change Tick: ax.set_xticks([0,5,10,15])                   # ax.set_yticks() same work with y-axis
    Change Tick Labels:                                       # ax.set_yticklabels() same work with y-axis
        ax.set_xticks([1,2,3,4])
        ax.set_xticklabels(
            ["Jan","Feb","Mar","Apr"]
        )
    Rotate Labels:                                            # ax.tick_params() same works with y-axis
        ax.tick_params(
            axis="x",
            rotation=45
        )
        
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 3,
                       constrained_layout=True,
                       figsize=(10,6), 
                       dpi=100, 
                       facecolor="lightyellow", 
                       edgecolor="blue", 
                       linewidth=2)

# fig.set_facecolor("lightgray")    # also set figure color like this.

ax[0,0].plot([1,2,3,4,5],[2,5,3,7,12])

ax[0,0].set_title("Line Plot")

ax[0,0].set_xlim(0,4)        
ax[0,0].set_ylim(0,20)




ax[0,0].set_xticks([1,2,3,4])
ax[0,0].set_xticklabels(
    ["Jan","Feb","Mar","Apr"]
    )

ax[0,0].tick_params(
    axis="x",
    rotation=45
)

# ax[0,0].set_xticks([1,2,3,4], ["Jan","Feb","Mar","Apr"], rotation=45)
#this change ticks, change labels and also rotate labels


plt.show()
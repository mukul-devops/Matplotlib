'''
- plt.figure() = - plt.figure() function is used to create a new figure object.
                 - Canvas setup before drawing.
                 - Useful when you want multiple plots in one script 
                   or need precise control over size and resolution.
                 - If you don’t call plt.figure(), Matplotlib automatically creates one for you.
                   But using it explicitly lets you customize things.

🔹 Common Parameters
    Parameter	        Purpose	                                        Example
    figsize	            Set figure size in inches (width, height)	    plt.figure(figsize=(8,5))
    dpi             	Resolution (dots per inch)	                    plt.figure(dpi=120)
    facecolor       	Background color of the figure              	plt.figure(facecolor="lightgray")
    edgecolor       	Border color of the figure                  	plt.figure(edgecolor="black")
    linewidth       	Thickness of border	                            plt.figure(linewidth=2)
    frameon         	Show/hide frame (default True)              	plt.figure(frameon=False)

    
                
'''

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [200, 250, 300, 280, 350]

plt.figure(figsize=(7,4), dpi=100, facecolor="lightyellow", edgecolor="blue", linewidth=2)

plt.plot(days, sales)
plt.show()



'''
🔹Understanding the Figure Lifecycle:
        plt.figure()       # Create a new figure
            ↓
        plt.plot()         # Add first line
            ↓
        plt.plot()         # Add second line
            ↓
        plt.title()
        plt.xlabel()
        plt.ylabel()
        plt.grid()
        plt.legend()
            ↓
        plt.show()         # Display everything
'''
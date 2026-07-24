'''
- plt.xticks() and plt.yticks() :
        These functions control the tick marks (the little numbers/labels along the axes) in your plot. 
        They let you customize positions and labels for both the X-axis and Y-axis.

    # Custom ticks
        plt.xticks([1, 2, 3, 4, 5], ["Jan", "Feb", "Mar", "Apr", "May"])
        The X-axis will show Jan, Feb, Mar, Apr, May instead of numbers.

🔹 Advanced Usage
    Rotate tick labels for readability:
        plt.xticks(rotation=45)

    Control font size and style:
        plt.xticks(fontsize=12, color="blue")
        plt.yticks(fontsize=12, color="green")        

           
        
'''

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

#Sets or gets the X-axis tick positions and labels.
plt.xticks([1, 2, 3, 4, 5], ["Jan", "Feb", "Mar", "Apr", "May"], fontsize=12, color="green")

#Sets or gets the Y-axis tick positions and labels.
plt.yticks([10, 20, 30, 40, 50], ["Low", "Medium", "High", "Very High", "Peak"], fontsize=12, color="green", rotation=45)

print(plt.xticks())   # Returns current positions and labels
print(plt.yticks())

plt.show()
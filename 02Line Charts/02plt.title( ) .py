'''
- plt.title() - The function plt.title() is used to add a title to your plot.
              This title appears at the top of the figure and describes what the chart is about.

🔹 Customization Options
    You can style the title with several parameters:

    plt.title("Customized Title", 
            fontsize=16,        # Text size
            fontfamily="serif"  # Text style
            color="purple",     # Text color
            loc="left",         # Position: 'left', 'center', 'right'
            fontweight="bold")  # Bold text

    fontsize → Controls size of the title text
    fontfamily → Change text style. Common families: "serif", "sans-serif", "monospace"
    color → Sets text color
    loc → Aligns title ("left", "center", "right")
    fontweight → "bold", "normal", "light" 

    By default size 12, black, centered, normal weight.             


'''

import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [200, 250, 300, 280, 350]

plt.plot(days, sales)

# plt.title("Daily Sales")
plt.title("Daily Sales",
          fontsize=16,
          fontfamily="serif",
          color="purple",
          loc="center",
          fontweight="bold"
          )

plt.show()